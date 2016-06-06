#!/usr/bin/python3.4
# -*- coding: utf-8 -*-



import subprocess
import os
import csv
#from Object import ClassName
from Haplotype import Haplotype
from Genotype import Genotype
import itertools as it


"""Functions used for reduicing main size
..."""
#################
######INPUT######
#################
def read_input_file(filename, objecttype, delimit):
	"""Return a list of objet by reading your input file,
	the type is determine by the argument "objecttype"

	Named parameter :
	-file -- Your input file
	-objecttype -- The type of objects you want by reading the file
	-delimit -- The delimiter of our file

	"""
	lst_of_objects = []
	with open(filename, 'r') as src :
		my_reader = csv.reader(src, delimiter=delimit)
		header = True
		for rows in my_reader :
			if header : 
				lst_markers = rows[1:]
				header = False
			else :
				A = objecttype(name=rows[0], sequence=rows[1:], markers=lst_markers)
				lst_of_objects.append(A)

	return lst_of_objects

##################
######OUTPUT######
##################
def compare_output(otp, firstobjcetlist, secondobjcetlist):
	"""Return nothing but give the csv output file with the compraison of 
	one sequence between a list of one. 

	Named parameters :
	-otp -- The output name
	-firstobjcetlist -- Can be a list of Genotypes objects or Haplotypes objects
	-secondobjcetlist -- A list of Haplotypes objects

	"""
	with open(otp, 'w') as otp_comparaison :
		my_otp_writer = csv.writer(otp_comparaison, delimiter="\t")

		header =[]
		header.append("Genotype")
		header.append("Haplotype")	
		for markers in firstobjcetlist[0].markers :
			header.append(markers)
		header.append("nb_errors")
		my_otp_writer.writerow(header)

		if firstobjcetlist == secondobjcetlist :
			for haplo1, haplo2 in it.combinations(firstobjcetlist, 2) :
				my_otp_writer.writerow(haplo1.compare_two_seq(haplo2))
		else :
			for geno, haplo in it.product(firstobjcetlist, secondobjcetlist) :
				my_otp_writer.writerow(geno.compare_two_seq(haplo))

#a delete (quand threshold sera fini et que tout marchera)
def compare_output_result(otp, listofgenoobject):
	"""Return nothing but give the csv output file with genotypes and them 
	similar haplotype (0 error find during the comparaison). 

	Named parameters :
	-otp -- The output name
	-listofgenoobject -- A list of Genotypes objects

	"""
	with open(otp, 'w') as otp_first_result :
		my_compare_selection = csv.writer(otp_first_result, delimiter="\t")
		
		#First row will be the header
		header =[]
		header.append("Genotype")
		header.append("Haplotype")	
		for markers in listofgenoobject[0].markers :
			header.append(markers)
		my_compare_selection.writerow(header)

		#After that we put our geno.name, is number of similar haplo and is sequence
		for geno in listofgenoobject:
			geno_compare_output = []
			geno_compare_output.append(geno.name)
			geno_compare_output.append(geno.number_of_similar_haplotype)
			for values in geno.sequence :
				geno_compare_output.append(values)
			my_compare_selection.writerow(geno_compare_output)

		#If my genotype have some similar haplotype (>0)
		#I put the haplotype name and his sequence under genotype sequence
			if geno.number_of_similar_haplotype > 0 :
				for similar_haplo in geno.similar_haplotype :
					haplo_compare_output = []
					haplo_compare_output.append("")
					haplo_compare_output.append(similar_haplo.name)
					for values in similar_haplo.sequence :
						haplo_compare_output.append(values)
					my_compare_selection.writerow(haplo_compare_output)

#good with threshlod
#a compléter si a le temps (add 2 colonnes : nb de correction pour les haplotypes candidat issue d'haplotypes corrigé/ et l'index d'où on lieu ces mismatch/correction)
def compare_output_result_test(otp, listofgenoobject):
	"""Return nothing but give the csv output file with genotypes and them 
	similar haplotype (0 error find during the comparaison). 

	Named parameters :
	-otp -- The output name
	-listofgenoobject -- A list of Genotypes objects

	"""
	with open(otp, 'w') as otp_first_result :
		my_compare_selection = csv.writer(otp_first_result, delimiter="\t")
		
		#First row will be the header
		header =[]
		header.append("Genotype")
		header.append("Haplotype")
		#header.append("nb_correction")
		#header.append("index_correction")
		for markers in listofgenoobject[0].markers :
			header.append(markers)
		my_compare_selection.writerow(header)

		#After that we put our geno.name, is number of similar haplo and is sequence
		for geno in listofgenoobject:
			geno_compare_output = []
			geno_compare_output.append(geno.name)
			geno_compare_output.append(len(geno.half_similarity_with[0]))
			for values in geno.sequence :
				geno_compare_output.append(values)
			my_compare_selection.writerow(geno_compare_output)

		#If my genotype have some similar haplotype (>0)
		#I put the haplotype name and his sequence under genotype sequence
			if len(geno.half_similarity_with[0]) > 0 :
				for candidate_haplo in geno.half_similarity_with[0] :
					haplo_compare_output = []
					haplo_compare_output.append(geno.name)
					haplo_compare_output.append(candidate_haplo.name)
					#haplo_compare_output.append(candidate_haplo.nb_mismatch)
					#haplo_compare_output.append(candidate_haplo.index_mismatch)
					for values in candidate_haplo.sequence :
						haplo_compare_output.append(values)
					my_compare_selection.writerow(haplo_compare_output)


def cytoscape_file(outputdir, lstofgenoobject):
	"""Return nothing but give a file that can be open with cytoscape software
	to see the interaction between genotype & haplotype.

	We maybe can see quickly haplotypes of interest (with multiple interaction with genotypes & haplotypes)

	"""
	#check the output file needed for the cytoscape software and my représentation 
	#did i need to specify a new column for haplo-haplo combinaison?
	with open(outputdir, 'w') as cyto_output :
		my_cytotp_writer = csv.writer(cyto_output, delimiter="\t")

		header = ['Source', 'Interaction_type', 'Target', 'Nb_of_missing_data', 'Haplo_origin']
		my_cytotp_writer.writerow(header)
		
		for geno in lstofgenoobject :
			if geno.number_of_similar_haplotype > 0 :
				for haplo in geno.similar_haplotype :
					source_target = [geno.name]
					source_target.append("g:h")
					source_target.append(haplo.name)
					source_target.append(haplo.missing_data)
					if "New" in haplo.name :
						source_target.append("new")
					else :
						source_target.append("known")
					my_cytotp_writer.writerow(source_target)
			else :
				source_target = [geno.name]
				my_cytotp_writer.writerow(source_target)




#Function for created the list of candidate haplo and the output
def new_haplotype_output(otp, lstofgenoobject):
	"""Return nothing but give an output with the Haplotype object containing the potential new haplotype
	(=candidates)

	Named parameters :
	-otp -- the output name
	-lstofgenoobject -- the list of Genotype object who contain potential new haplotype

	"""
	with open(otp, 'w') as otp3 :
		my_new_H_otp_writer = csv.writer(otp3, delimiter="\t")

		#Creation of the header of my output
		header = ["Genotype", "Haplotype", "Candidate_Haplotype"]
		for markers in lstofgenoobject[0].markers :
			header.append(markers)
		my_new_H_otp_writer.writerow(header)

		#Add eatch row containing a new haplotype (where he come from, his name and his sequence)
		for geno in lstofgenoobject :
			if geno.number_of_new_created_haplotype > 0 :
				for i in range(len(geno.lst_of_new_haplotype)) :
					candidate_haplo_output = []
					candidate_haplo_output.append(geno.name)
					candidate_haplo_output.append((geno.lst_of_new_haplotype[i]).name)
					candidate_haplo_output.append("New:{}//{}".format( geno.name, (geno.lst_of_new_haplotype[i]).name)) 
					for values in geno.lst_of_new_haplotype[i].sequence :
						candidate_haplo_output.append(values)

					#I write my output where i can find the sequence of all my new haplotype in row
					my_new_H_otp_writer.writerow(candidate_haplo_output)

#this one the filtred candidate haplotype
def uniq_candidate_haplo(otp, lstuniqhaplo):
	with open(otp, 'w') as uniq_new :
		my_otp_uniq_new_writer = csv.writer(uniq_new, delimiter="\t")

		header = ["candidate_name"]
		for markers in lstuniqhaplo[0].markers :
			header.append(markers)
		my_otp_uniq_new_writer.writerow(header)

		for candidate in lstuniqhaplo :
			candidate_haplo_output = []
			candidate_haplo_output.append(candidate.name)
			for nt in candidate.sequence :
				candidate_haplo_output.append(nt)
			my_otp_uniq_new_writer.writerow(candidate_haplo_output)









#change to do it with a dicotionnary
#need change this one or a previous one to know when i use haplotype with >0 mismatch 
#A DELETE
def new_haplotype(lstofgenoobject):
	"""Return a list of Haplotype object containing the potential new haplotype (=candidates)
	We give for this candidate the name with the prefix "New:" and the genotype and haplotype names
	needed for his construction. Those one are separate by "//"

	Named parameters :
	-lstofgenoobject -- the list of Genotype object who contain potential new haplotype

	"""
	lst_of_haplo_object_expanded = []

	lst_markers = []
	for markers in lstofgenoobject[0].markers :
		lst_markers.append(markers)

	for geno in lstofgenoobject :
		if geno.number_of_new_created_haplotype > 0 :
			for i in range(len(geno.lst_of_new_haplotype)) :
				my_new_haplo = []
				my_new_haplo.append("New:{}//{}".format(geno.name, (geno.similar_haplotype[i]).name)) 
				#pouvoir indiquer ici si mon haplo est corrigé ou non.
				for values in geno.lst_of_new_haplotype[i] :
					my_new_haplo.append(values)		
				A = Haplotype(name=my_new_haplo[0], sequence=my_new_haplo[1:], markers=lst_markers)
				lst_of_haplo_object_expanded.append(A)

	return lst_of_haplo_object_expanded

#Important d'avoir le nom de l'haplotype après // pour savoir si il avait une erreur avant
#pb c'est que je met tous mes nouveaux haplo dans une liste sans savoir s'ils ont une erreur de corrigée ou plus
#fonctionne mais difficulter pour accéder au nom de l'haplo
#A DELETE
def new_haplotype_test(lstofgenoobject):
	"""Return a list of Haplotype object containing the potential new haplotype (=candidates)
	We give for this candidate the name with the prefix "New:" and the genotype and haplotype names
	needed for his construction. Those one are separate by "//"

	Named parameters :
	-lstofgenoobject -- the list of Genotype object who contain potential new haplotype

	"""
	lst_of_haplo_object_expanded = []

	lst_markers = []
	for markers in lstofgenoobject[0].markers :
		lst_markers.append(markers)

	for geno in lstofgenoobject :
		if geno.number_of_new_created_haplotype > 0 :
			for i in range(len(geno.lst_of_new_haplotype)) :
				my_new_haplo = []
				my_new_haplo.append("New:{}//{}".format(geno.name, "temporaire"+str(i))) #pb ici pour lui donner le nom de l'haplotype (dans un dico)
				#pouvoir indiquer ici si mon haplo est corrigé ou non.
				for values in geno.lst_of_new_haplotype[i] :
					my_new_haplo.append(values)		
				A = Haplotype(name=my_new_haplo[0], sequence=my_new_haplo[1:], markers=lst_markers)
				lst_of_haplo_object_expanded.append(A)

	return lst_of_haplo_object_expanded

#########################
######FUNCTION HELP######
#########################
#a conserver
#new one to replace the 2 previous
def new_haplotype_test_extend(lstofgenoobject):
	extend_lst = []
	for geno in lstofgenoobject :
		extend_lst.extend(geno.lst_of_new_haplotype)
	return extend_lst




#Les deux fonctions suivantes sont la pour avoir des info sur le nombre de fois qu'un haplotype est trouvé similaire a un génotype
#Possibilité de la réduire en une avec une condition pour savoir ce que je traite
def haplotype_redundancy(otp, lstofhaplo):
	"""Return nothing but give an output of occurency hmz haplotype be similar 
	with our genotypes.

	"""
	with open(otp, 'w') as redundancy_src :
		my_redundancy_writer = csv.writer(redundancy_src, delimiter="\t")

		header =  ['Name', 'Redundancy', 'Frequency'] #maybe give the freq directly here
		my_redundancy_writer.writerow(header)
		for haplo in lstofhaplo: #pas très logique ici 
			redundancy = []
			redundancy.append(haplo.name)
			redundancy.append(haplo.similar_occurence)
			redundancy.append(haplo.frequency)
			my_redundancy_writer.writerow(redundancy)

#for my violin plot
def new_haplotype_occurency(otp, lstofscreeninghaplo, lstofnoconfirmedgeno):
	"""Return nothing but give an output of occurency the new haplotype be similar 
	with our genotypes

	"""
	with open(otp, 'w') as occurency_src :
		my_occurency_writer = csv.writer(occurency_src, delimiter="\t")

		header =  ['Name', 'run1_occurency', 'run2_redundancy', 'missing_data']
		my_occurency_writer.writerow(header)
		for haplo in lstofscreeninghaplo:
			occurency = []
			haplo.similar_occurence = haplo.similarity_time_with()
			occurency.append(haplo.name)
			occurency.append((haplo.number_of_similar_new_haplotype)+1)
			occurency.append(haplo.similar_occurence)
			occurency.append(haplo.missing_data)
			my_occurency_writer.writerow(occurency)


#Funtion use for read another script language
def run_R_file(path2file, outputdir):
	"""This function return the result you obtain with your R file

	Named parameters :
	-path2file -- the path to the file to read
	-outputdir -- the path to write the output of the reading file

	"""
	command = 'Rscript'
	path2script = os.path.join(os.path.curdir, path2file)
	setwd = [os.path.abspath(os.path.join(os.path.curdir, outputdir))]
       
	cmd = [command, path2script] + setwd
	x = subprocess.Popen(cmd, stderr=subprocess.PIPE)
	return x.communicate()



















######SUMMARY######
#Pour les 2 fonctions suivante penser a break quand on a atteint le nombre de génotype
def mismatch_distribution(lstofhaplotype, filetoread):
	"""Soit en utilisant les sorties 1 et 4 
	ou en refaisant la méthode dans génotype"""
	distribution_dictionnary = {}

	for i in range(len(lstofhaplotype[0].sequence)+1):
		distribution_dictionnary[i] = 0
	
	with open(filetoread, 'r') as distri_src :
		my_distri_reader = csv.reader(distri_src, delimiter="\t")
		
		header = True
		for rows in my_distri_reader :
			if header :
				header = False
			else :
				distribution_dictionnary[int(rows[-1])] +=1

	return distribution_dictionnary

def mismatch_distribution_output(otp, distri_dictionary):
	"""Return nothing but do the necesary otp for R distribution"""
	with open(otp, 'w') as distri_otp :
		my_distri_writer = csv.writer(distri_otp, delimiter="\t")

		header = ['Number_of_mismatch', 'Number_of_mismatch_occurency']
		my_distri_writer.writerow(header)
		for key, value in distri_dictionary.items() :
			my_distri_writer.writerow([key, value])





def mismatch_location(lstofhaplotype, filetoread):
	"""Return un dictionnaire avec par marqueur le nombre de mismatch observé"""
	distri_loca_dico = {}

	#dictionary who have a number of keys equal to the marker number
	for imarker in range((lstofhaplotype[0].nbmarkers)+1) :
		# +2 to have the column of the markers
		distri_loca_dico[imarker+2] = 0

	with open(filetoread) as distri_loca_src :
		my_distri_loca_dico_writer = csv.reader(distri_loca_src, delimiter="\t")

		header=True
		for rows in my_distri_loca_dico_writer :
			if header:
				header=False
			else :
				for marker in rows[2:-1] :
					if marker == "1" :
						distri_loca_dico[marker] += 1

	return distri_loca_dico


def mismatch_location_output(otp, loca_dictionary):
	"""Return nothing but give us the necesary output for R distribution """
	with open(otp, 'w') as loca_otp :
		my_loca_otp = csv.writer(loca_otp, delimiter="\t")

		header = []



#FUNCTION FOR MY GENERAL SUMMARY

#rappel de la commande utilisée
#version
#nombre d'haplotype known candidate fastPHASE
#nombre de bonne combi avec known seul puis avec candidate
#nombre de known réellement utilisé (freqs)
#si possible les haplotypes a conserver après les runs
	#si freq élevé voir même si bien classé après fastPHASE

#Function for the summary of the résult
def probable_haplotypes_combinaison_counter(self, lstofhaploobject, lstofgenoobject):
	"""Return a dictionnary with the number of eatch probable combination
	and this for eatch number of similar haplotype that our genotypes have

	keys is the number of similar haplotype 
	values is a list countaining the number of probable haplotype combination
	(there index are the number of possible combination)

	Named parameter: 
	-lstofgenoobject :  the list of Genotype objects

	"""
	dico = {}

	#for geno in lstofgenoobject:


	#key = number of similar haplotype for our génotypes
	#values = [nb, nb, nb] index [0, 1, 2] are the probable good combination observed
	#penser a mettre la somme de geno pour chaque keys

	return dico
	#and now i just need a fonction who organize a output with this dico

##FONCTIONS A ENVISAGER
	#lecture des inputs
	#Ecriture des différentes sorties
		#1) erreurs between 2 seq (run 1 haplo/geno (et halo/haplo si --dist))(et run2 newhaplo/geno)
		#2) genotype et halotypes similaire associé (run 1 et 2)
		#3) nouvx haplo (end run 1)
	#Les runs
		#1
		#2

##DANS Haplotype rebuilding (main)
	#docopt et conditions plus utilisation des fonctions ci dessus.


def count_genotype_with_same_number_of_similar_haplotype(genotype, theNumber) :
	"""Use for count the number of génotypes with the same number of similar haplotypes

	Named parameters :
	genotype -- a Genotype object
	theNumber -- a int between 0 to 84 (len(lst_of_haplo_object)
	
	"""
	if genotype.number_of_similar_haplotype == theNumber:
		count = 1
	else :
		count = 0
	return count