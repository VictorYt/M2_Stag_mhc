#!/usr/bin/env python
# -*- coding: utf-8 -*-


from csv import reader, writer
from sys import argv
#from Object import ClassName
from Haplotype import Haplotype
from Genotype import Genotype


"""Functions used for reduicing main size
..."""


#Ou créer un fichier 'fonction_utilites'  
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
				lst_markers = rows[1:len(rows)]
				count = False
			else :
				A = objecttype(name=rows[0], sequence=rows[1:len(rows)], markers=lst_markers)
				lst_of_objects.append(A)
		src.close()

	return lst_of_objects






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



		otp3.close()


	return lst_of_haplo_object_expanded








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