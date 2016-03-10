#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Tout traduire en anglais
"""Programme de reconstruction d'haplotype 
..."""


#A faire
	#Gérer les options -i -o etc ... (docpot)
	#vérifier les combinaisons haplo/haplo pour obtenir notre geno
	#Sorties (brut/rangée/comme on souhaite les avoir/...)


#Nécessite de décrire le format d'input des 2 entrées.

import time
from csv import reader, writer
from sys import argv
#from Object import ClassName
from Haplotype import Haplotype
from Genotype import Genotype




################
#SOME FONCTIONS# importe un used(utile) from used import *
################

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












"""Création de 2 listes d'objets
La premire, lst_of_haplo_object, contient les n objets Haplotype
La seconde, lst_of_geno_object, contient les n objets Genotype"""
#Réorganiser le main
if __name__ == '__main__':
	debut1 = time.time()
	print ("\nLes histoires commencent  :")
	lst_of_haplo_object = []
	lst_of_geno_object = []
	lst_markers_haplo = None
	lst_markers_geno = None
	delimit = "\t"
	haplotype = argv[1]
	genotype = argv[2]
	first_output = argv[3]
	second_output = argv[4]
	third_output = argv[5]
	fourst_output = argv[6]
	first_txt_output = argv[7]

	with open(haplotype, 'r') as src_haplo, open(genotype, 'r') as src_geno :
		my_haplo_reader = reader(src_haplo, delimiter=delimit)
		my_geno_reader = reader(src_geno, delimiter=",")
		#my_otp1_writer = writer(otp1, delimiter = delimit)

		#Compteur utilisé pour la récupération du header
		count1 = True
		count2 = True

		"""Construction de ma lst_of_haplo_object"""
		for rows in my_haplo_reader :
			if count1 : #Si booleen est vrai
				lst_markers_haplo = rows[1:80]
				count1 = False
			else :
				A = Haplotype(name=rows[0], sequence=rows[1:80], markers=lst_markers_haplo)
				lst_of_haplo_object.append(A)
		#print ("Nombre d'objet haplo :",len(lst_of_haplo_object))


		""" Construction de ma lst_of_geno_object"""
		for rows in my_geno_reader :
			if count2 : #Si booleen est vrai
				lst_markers_geno = rows[1:80]
				count2 = False
			else :
				B = Genotype(name=rows[0], sequence=rows[1:80], markers=lst_markers_geno)
				lst_of_geno_object.append(B)
		#print ("Nombre d'objet geno :",len(lst_of_geno_object))



		"""Récupératoin du nombre de markers Hmz et Htz par génotype avec en plus l'index des position Htz"""
		print ("Les marqueurs des genotypes sont {}:".format(lst_of_geno_object[1].markers))
		for geno in lst_of_geno_object :
			#print ("Le genotype {}, constitué de {} marqueurs, à pour sequence \n{}".format(geno.name, geno.nbmarkers, geno.sequence))
			geno.index_htz_markers_in_seq = (geno.position_htz_markers())
			geno.nb_htz_markers = geno.have_nb_htz_markers()
			geno.nb_hmz_markers = geno.have_nb_hmz_markers()
			#print ("il a {} marqueurs Hmz et {} Htz".format(geno.nb_hmz_markers, geno.nb_htz_markers))



		src_haplo.close()
		src_geno.close()



	#A partir d'ici j'ai Ma liste d'Haplo et de Geno
	#voir pour interprétation des unknowing markers (new branche in git) va se traiter comme A/B sauf que là tout le temps = 0 ici tout le temps =0
	"""Comparaison 1 par 1 des génotype avec la liste des haplotype"""


	#ouverture des fichiers pour les 2 premières sorties
	with open(first_output, 'w') as otp1, open(second_output, 'w') as otp2 :
		my_otp1_writer = writer(otp1, delimiter=delimit)
		my_otp2_writer = writer(otp2, delimiter=delimit)

		
	#écriture de la première sortie
		for geno in lst_of_geno_object :
			for haplo in lst_of_haplo_object :
				geno.select_similar_haplotype(geno, haplo)
				geno.number_of_similar_haplotype = len(geno.similar_haplotype)
				#écriture ce fait ici
				my_otp1_writer.writerow(geno.compare_two_seq(geno, haplo))

		otp1.close()



	#écriture de la seconde sortie (à revoir pas clair à la lecture)
		lst_header =[]
		lst_header.append("Genotype")
		lst_header.append("Haplotype")	
		for markers in lst_of_geno_object[0].markers :
			lst_header.append(markers)
		my_otp2_writer.writerow(lst_header)


		for geno in lst_of_geno_object:
			geno_second_sortie = []
			geno_second_sortie.append(geno.name)
			geno_second_sortie.append(geno.number_of_similar_haplotype)
			for values in geno.sequence :
				geno_second_sortie.append(values)
			my_otp2_writer.writerow(geno_second_sortie)

			
			if geno.number_of_similar_haplotype > 0 :
				for similar_haplo in geno.similar_haplotype :
					haplo_second_sortie = []
					haplo_second_sortie.append(geno.name)
					haplo_second_sortie.append(similar_haplo.name)
					for values in similar_haplo.sequence :
						haplo_second_sortie.append(values)
					my_otp2_writer.writerow(haplo_second_sortie)
				my_otp2_writer.writerow("\n")
			else : 
				my_otp2_writer.writerow("\n")
			
		otp2.close()





	#Utilisation de la fonction créer au dessus
	count_geno = 0
	count = 0
	for i in range((len(lst_of_haplo_object)+1)) :
		count_geno += count
		count = 0
		for geno in lst_of_geno_object :
			count += count_genotype_with_same_number_of_similar_haplotype(genotype=geno, theNumber=i)
		if count_geno < len(lst_of_geno_object) :		
			print ("Les genotypes avec {} haplotype(s) commun(s) sont au nombre de {}".format(i, count))



	"""Manip permettant d'avoir le nombre de combinaison viable en fonction du nombre d'haplotype possible"""
	#Création de nouveaux haplotypes à partir des génotypes et un haplotypes simailaire

	nb_total_new_h = 0 #compteur pour avoir le nombre total d'haplotype construit
	for geno in lst_of_geno_object :
		#Parmi les haplotype similaire à notre génotype, lesquels combiné l'un avec l'autre redonne le génotype
		geno.probable_haplotypes_combinaison = geno.combinaison_between_similar_haplotype_in_geno()
		#Le nombre de combinaison obtenues ci-dessus sont possible pour notre génotype.
		geno.number_of_probable_haplotypes_combinaison = len(geno.probable_haplotypes_combinaison)
		#création des nouveaux haplotypes à l'aide de la méthode .have_new_haplotype()
		#et stockage dans l'attribut lst_of_new_haplotype
		geno.lst_of_new_haplotype = geno.have_new_haplotype() 
		geno.number_of_new_created_haplotype = len(geno._lst_of_new_haplotype)

		#Sommage du compteur, dans la boucle
		nb_total_new_h += geno.number_of_new_created_haplotype
	print ("le nombre total d'haplo créé est de  : {}".format(nb_total_new_h))	
		




	#écriture de la troisième sortie (liste des nouveau haplotype créé)
	with open(third_output, 'w') as otp3 :
		my_otp3_writer = writer(otp3, delimiter=delimit)

		lst_header =[]
		lst_header.append("Genotype")
		lst_header.append("Haplotype")
		lst_header.append("New_Haplotype")	
		for markers in lst_of_geno_object[0].markers :
			lst_header.append(markers)
		#ecriture de l'en-tête de l'output n°3
		my_otp3_writer.writerow(lst_header)


		for geno in lst_of_geno_object :
			if geno.number_of_new_created_haplotype > 0 :
				for i in range(len(geno.lst_of_new_haplotype)) :
					third_sortie = []
					third_sortie.append(geno.name)
					third_sortie.append((geno.similar_haplotype[i]).name)
					third_sortie.append("new{}_G:{}:H:{}".format(i+1, geno.name, (geno.similar_haplotype[i]).name)) 
					for values in geno.lst_of_new_haplotype[i] :
						third_sortie.append(values)
					my_otp3_writer.writerow(third_sortie)
	#Sur les 274 nouveaux haplotypes généré il y a 246 réellement différents
		otp3.close()





	"""Comparaison des haplotypes les uns par rapport aux autres 
	pour pouvoir comparer leur distribution avec celle des génotypes"""

	#ouverture et écriture du quatrième fichier 
	with open(fourst_output, 'w') as otp4 :
		my_otp4_writer = writer(otp4, delimiter=delimit)

	#écriture de la quatrième sortie
		#parcourt des n(n-1)/2 combinaisons entre haplotypes possibles
		for haplo1 in range(len(lst_of_haplo_object)-1) :
			for haplo2 in range((haplo1+1),len(lst_of_haplo_object)) :
				my_otp4_writer.writerow(lst_of_haplo_object[haplo1].compare_two_seq(lst_of_haplo_object[haplo1], lst_of_haplo_object[haplo2]))

		otp4.close()


#Essayer de traité directement cette sortie pour avoir 2 autres sorties utiles pour avoir la distribution des erreurs
























	#Penser a faire une fonction qui pourrait me donner ces résultats
	count_2_0 = 0
	count_2_1 = 0

	count_3_0 = 0
	count_3_1 = 0
	count_3_2 = 0
	count_3_3 = 0

	count_4_0 = 0
	count_4_1 = 0
	count_4_2 = 0

	count_5_0 = 0
	count_5_1 = 0

	count_6_0 = 0
	count_6_1 = 0
	count_6_2 = 0
	count_6_3 = 0


	for geno in lst_of_geno_object :
		if geno.number_of_similar_haplotype == 2 : 
			if geno.number_of_probable_haplotypes_combinaison == 0 :
				count_2_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison == 1 :
				count_2_1 +=1
		
		elif geno.number_of_similar_haplotype == 3 :
			if geno.number_of_probable_haplotypes_combinaison == 0 :
				count_3_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison == 1 :
				count_3_1 +=1
			elif geno.number_of_probable_haplotypes_combinaison == 2 :
				count_3_2 += 1
			elif geno.number_of_probable_haplotypes_combinaison == 3 :
				count_3_3 += 1
		
		elif geno.number_of_similar_haplotype == 4 :
			if geno.number_of_probable_haplotypes_combinaison == 0 :
				count_4_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison == 1 :
				count_4_1 +=1
			elif geno.number_of_probable_haplotypes_combinaison == 2 :
				count_4_2 += 1

		elif geno.number_of_similar_haplotype == 5 :
			if geno.number_of_probable_haplotypes_combinaison == 0 :
				count_5_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison == 1 :
				count_5_1 +=1

		elif geno.number_of_similar_haplotype == 6 :
			if geno.number_of_probable_haplotypes_combinaison == 0 :
				count_6_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison == 1 :
				count_6_1 += 1
			elif geno.number_of_probable_haplotypes_combinaison == 2 :
				count_6_2 += 1
			elif geno.number_of_probable_haplotypes_combinaison == 3 :
				count_6_3 += 1

	print ("\n\nSi 2 haplotypes similaires au géno :\n{} ne donne rien \n{} combinent et donne le génotype".format(count_2_0, count_2_1))
	print ("\n\nSi 3 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont les 3 combinaisons possible".format(count_3_0, count_3_1, count_3_2, count_3_3))
	print ("\n\nSi 4 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons".format(count_4_0, count_4_1, count_4_2))
	print ("\n\nSi 5 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison ".format(count_5_0, count_5_1))
	print ("\n\nSi 6 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont 3 combinaison ".format(count_6_0,count_6_1, count_6_2, count_6_3))



	#Sortie txt générale.
	with open(first_txt_output,'w') as txt_otp1 :
		txt_otp1.write("Noms des fichiers passés en input : \nPour les haplotypes : {}\nPour les génotypes : {}".format(haplotype, genotype))
		txt_otp1.write("\nNombre d'objet Haplotype créé : {}".format(len(lst_of_haplo_object)))
		txt_otp1.write("\nNombre d'objet Genotype créé : {}".format(len(lst_of_geno_object)))
		txt_otp1.write("\nSéquences composées de {} marqueurs".format(len(lst_of_geno_object[1].markers)))
		txt_otp1.write("\nLes marqueurs des genotypes sont {}:".format(lst_of_geno_object[1].markers))
		txt_otp1.write("\n\nSi 2 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} on une combinaison qui redonne le génotype".format(count_2_0, count_2_1))
		txt_otp1.write("\nSi 3 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont les 3 combinaisons possible".format(count_3_0, count_3_1, count_3_2, count_3_3))
		txt_otp1.write("\nSi 4 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} ont 1 combinaison \n{} ont 2 combinaisons".format(count_4_0, count_4_1, count_4_2))
		txt_otp1.write("\nSi 5 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} ont 1 combinaison ".format(count_5_0, count_5_1))
		txt_otp1.write("\nSi 6 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} ont 3 combinaisons \n\n\n\n".format(count_6_0, count_6_3))
		
		for geno in lst_of_geno_object :
			if geno.number_of_probable_haplotypes_combinaison > 1 :
				txt_otp1.write("\n\nProbleme de combinaison pour le génotype : {}".format(geno.name))
				txt_otp1.write("\nVérification des combinaison suivante : {}".format(geno.probable_haplotypes_combinaison))


	fin1 = time.time()
	temps1 = fin1 - debut1
	print ("\n\n\nLe temps d'execution du premier run est de : {}".format(temps1))


	debut2 = time.time()



	
			





































	"""Second run without genotype who can be explain by knowning haplotype and with the new haplotype created in the 1st run """
	
	#List of Genotypes Objects no confirmed by the 1st run (genotype_non_confirmed)
	#We keep genotypes confirmes in another list (genotype_confirmed)
	lst_genotype_confirmed = []
	lst_genotype_non_confirmed = []
	for geno in lst_of_geno_object :
		if geno.number_of_new_created_haplotype == 0 and geno.number_of_similar_haplotype > 1 :
			lst_genotype_confirmed.append(geno)
		else : 
			lst_genotype_non_confirmed.append(geno)

	

	#We expanded the Haplotype objects list with the new_haplotypes
	#lst_of_haplo_object_all ==> containing all the haplo
	#lst_of_haplo_object_expanded ==> containing new halpo
	with open(third_output,'r') as new_H :
		my_new_H_reader = reader(new_H, delimiter=delimit)

		header = True
		lst_of_haplo_object_expanded = []
		for new_haplotypes in my_new_H_reader : 
			if header :
				header = False
				pass
			else :
				A = Haplotype(name=new_haplotypes[2], sequence=new_haplotypes[3:82], markers=lst_markers_haplo)
				lst_of_haplo_object_expanded.append(A)
		lst_of_haplo_object_all = lst_of_haplo_object + lst_of_haplo_object_expanded
	
	print(len(lst_of_haplo_object))
	print(len(lst_of_haplo_object_expanded))
	print(len(lst_of_haplo_object_all))
	print(len(lst_genotype_non_confirmed))

	#Add new_haplo which are similar to our genotype no confirmed to the list of similar_haplotype
	#And change the number of similar haplotype

	for geno_non_confirmed in lst_genotype_non_confirmed :
		for new_haplo in lst_of_haplo_object_expanded :
			#Repérage des new_haplo identique aux genotypes restant
			geno_non_confirmed.select_similar_haplotype(geno_non_confirmed, new_haplo)
			#Changer de nombre d'haplo similaire (faire une diff entre les deux a ce niveau?)
			geno_non_confirmed.number_of_similar_haplotype = len(geno_non_confirmed.similar_haplotype)
			#écriture ce fait ici (faire le nouveau fichier de sortie)
			#my_otpx_writer.writerow(geno_non_confirmed.compare_two_seq(geno_non_confirmed, new_haplo))
	
	#petite vérification
	#for g in lst_genotype_non_confirmed :
	#	print("\ngeno : {} ".format(g.name))
	#	print("les haplotype sim sont :")
	#	print(g.number_of_similar_haplotype)
	#	for i in range(len(g.similar_haplotype)):
	#		print((g.similar_haplotype)[i].name)

	#otpx.close()




	count_geno_non_confirmed = 0
	count = 0
	for i in range((len(lst_of_haplo_object_all)+1)) :
		count_geno_non_confirmed += count
		count = 0
		for geno_non_confirmed in lst_genotype_non_confirmed :
			count += count_genotype_with_same_number_of_similar_haplotype(genotype=geno_non_confirmed, theNumber=i)
		if count_geno_non_confirmed < len(lst_genotype_non_confirmed) :		
			print ("Les genotypes avec {} haplotype(s) commun(s) sont au nombre de {}".format(i, count))






#A partir de la il faut

	#Reparcourir lst_geno_objet et créer une nouvelle liste sans les geno retrouver avec nos haplotypes (309 geno)
	#Mettre dans le fichier texte le nombre et le nom des genotypes pour lesquels les haplotypes connues permettent de les décrires
	#Ajouter à la liste des haplo les nvx haplo(tous?) ---> tous ici
	#2ème run avec d'autres fichier d'output
		#peut être faire un main avec run et ecriture d'output séparé (écriture d'output dans une fonction, comme ça 2ème run juste changer les arguments)


	fin2 = time.time()
	temps2 = fin2 - debut2
	print ("\n\n\nLe temps d'execution du second run est de : {}".format(temps2))


#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!