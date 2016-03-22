#!/usr/bin/env python
# -*- coding: utf-8 -*-


from csv import reader, writer
from sys import argv
#from Object import ClassName
from Haplotype import Haplotype
from Genotype import Genotype
from itertools import product, combinations


"""Functions used for reduicing main size
..."""


  
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
		my_reader = reader(src, delimiter=delimit)
		count = True
		for rows in my_reader :
			if count : 
				lst_markers = rows[1:]
				count = False
			else :
				A = objecttype(name=rows[0], sequence=rows[1:], markers=lst_markers)
				lst_of_objects.append(A)
		src.close()

	return lst_of_objects


def compare_output(otp, firstobjcetlist, secondobjcetlist):
	"""Return nothing but give the csv output file with the compraison of 
	one sequence between a list of one. 

	Named parameters :
	-otp -- The output name
	-firstobjcetlist -- Can be a list of Genotypes objects or Haplotypes objects
	-secondobjcetlist -- A list of Haplotypes objects

	"""
	with open(otp, 'w') as otp_comparaison :
		my_otp_writer = writer(otp_comparaison, delimiter="\t")

		lst_header =[]
		lst_header.append("Genotype")
		lst_header.append("Haplotype")	
		for markers in firstobjcetlist[0].markers :
			lst_header.append(markers)
		lst_header.append("nb_errors")
		my_otp_writer.writerow(lst_header)

		if firstobjcetlist == secondobjcetlist :
			for haplo1, haplo2 in combinations(firstobjcetlist, 2) :
				my_otp_writer.writerow(haplo1.compare_two_seq(haplo1, haplo2))
		else :
			for geno, haplo in product(firstobjcetlist, secondobjcetlist) :
				my_otp_writer.writerow(geno.compare_two_seq(geno, haplo))


def compare_output_result(otp, listofgenoobject):
	"""Return nothing but give the csv output file with genotypes and them 
	similar haplotype (0 error find during the comparaison). 

	Named parameters :
	-otp -- The output name
	-listofgenoobject -- A list of Genotypes objects

	"""
	with open(otp, 'w') as otp_first_result :
		my_compare_selection = writer(otp_first_result, delimiter="\t")
		
		#First row will be the header one
		lst_header =[]
		lst_header.append("Genotype")
		lst_header.append("Haplotype")	
		for markers in listofgenoobject[0].markers :
			lst_header.append(markers)
		my_compare_selection.writerow(lst_header)

		#After that we put our geno.name is number of similar haplo and is sequence
		for geno in listofgenoobject:
			geno_second_output = []
			geno_second_output.append(geno.name)
			geno_second_output.append(geno.number_of_similar_haplotype)
			for values in geno.sequence :
				geno_second_output.append(values)
			my_compare_selection.writerow(geno_second_output)

		#If my genotype have some similar haplotype (>0)
		#I put the haplotype name and his sequence under genotype sequence
			if geno.number_of_similar_haplotype > 0 :
				for similar_haplo in geno.similar_haplotype :
					haplo_second_output = []
					haplo_second_output.append("")
					haplo_second_output.append(similar_haplo.name)
					for values in similar_haplo.sequence :
						haplo_second_output.append(values)
					my_compare_selection.writerow(haplo_second_output)



#Functionfor created the list of new_haplo and the 3rd output
def new_haplotype_output(otp, lstofgenoobject):
	"""Return a list of Haplotype object containing the potential new haplotype

	Named parameters :
	-otp -- the output name
	-lstofgenoobject -- the list of Genotype object who contain potential new haplotype

	"""
	lst_of_haplo_object_expanded = []
	
	with open(otp, 'w') as otp3 :
		my_new_H_otp_writer = writer(otp3, delimiter="\t")

		#Creation of the header of my output
		lst_header= []
		lst_header.append("Genotype")
		lst_header.append("Haplotype")
		lst_header.append("New_Haplotype")
		for markers in lstofgenoobject[0].markers :
			lst_header.append(markers)
		my_new_H_otp_writer.writerow(lst_header)

		#Add eatch row containing a new haplotype (where he come from, his name and his sequence)
		for geno in lstofgenoobject :
			if geno.number_of_new_created_haplotype > 0 :
				for i in range(len(geno.lst_of_new_haplotype)) :
					third_sortie = []
					third_sortie.append(geno.name)
					third_sortie.append((geno.similar_haplotype[i]).name)
					third_sortie.append("New:{}//{}".format( geno.name, (geno.similar_haplotype[i]).name)) 
					for values in geno.lst_of_new_haplotype[i] :
						third_sortie.append(values)

					#Here i append to my list of new haplotype the potential new haplotype i can have
					A = Haplotype(name=third_sortie[2], sequence=third_sortie[3:len(third_sortie)], markers=lst_header[3:len(third_sortie)])
					lst_of_haplo_object_expanded.append(A)

					#I write my output where i can find the sequence of all my new haplotype in row
					my_new_H_otp_writer.writerow(third_sortie)


	return lst_of_haplo_object_expanded



#Change the name of the fonction to be more specific



def error_distribution(lstofhaplotype, filetoread):
	"""Soit en utilisant les sorties 1 et 4 
	ou en refaisant la méthode dans génotype"""
	distribution_dictionnary = {}

	for i in range(len(lstofhaplotype[0].sequence)+1):
		distribution_dictionnary[i] = 0
	
	with open(filetoread, 'r') as distri_src :
		my_distri_reader = reader(distri_src, delimiter="\t")
		
		header = True
		for rows in my_distri_reader :
			if header :
				header = False
			else :
				distribution_dictionnary[int(rows[-1])] +=1

	return distribution_dictionnary


def error_distribution_output(distri_dictionary):
	"""Return nothing but do the necesary otp for R distribution"""
	#with open(otp, 'w') as distri_otp :
	#	my_distri_writer = writer(distri_otp, delimiter="\t")

	for key in distri_dictionary :
		print(key[0], key[1])
		#my_distri_writer.writerow(key)


def new_haplotype_occurency(otp, lstofscreeninghaplo, lstofnoconfirmedgeno):
	"""Return nothing but give an output of occurency the new haplotype be similar 
	with our genotypes

	"""
	with open(otp, 'w') as occurency_src :
	my_occurency_writer = writer(occurency_src, delimiter="\t")

	header =  [Name, run1_occurency, run2_occurency]
	my_occurency_writer.writerow(header)
	for haplo in lstofscreeninghaplo:
		occurency = []
		haplo.similar_occurence = haplo.occurence_new_haplotype(lstofnoconfirmedgeno)
		occurency.append(haplo.name)
		occurency.append((haplo.number_of_similar_new_haplotype)+1)
		occurency.append(haplo.similar_occurence)
		my_occurency_writer.writerow(occurency)

def geom_plot():
	"""Avec la dernière sortie et occurence des new haplotype (voir aussi pour hmz)
	faire appel a R et lancer la réalisation du graph geom_plot
	"""
	#call subprocess 
	#Do R script here
	pass






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