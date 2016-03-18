#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Tout traduire en anglais
"""Programme de reconstruction d'haplotype 
..."""


#A faire
	#Gérer les options -i -o etc ... (docpot)
	#vérifier les combinaisons haplo/haplo pour obtenir notre geno (si -dist) 


#Nécessite de décrire le format d'input des 2 entrées.

import time
from csv import reader, writer
from sys import argv
#from Object import ClassName, function ...
from Haplotype import Haplotype
from Genotype import Genotype
from used_function import *





"""Création de 2 listes d'objets
La premire, lst_of_haplo_object, contient les n objets Haplotype
La seconde, lst_of_geno_object, contient les n objets Genotype"""
#Réorganiser le main
if __name__ == '__main__':
	debut1 = time.time()
	print ("\nLes histoires commencent  :")
	lst_of_haplo_object = None
	lst_of_geno_object = None
	lst_markers_haplo = None
	delimit = "\t"
	haplotype = argv[1]
	genotype = argv[2]
	first_output = "first_"+argv[3]
	second_output = "second_"+argv[3]
	third_output = "third_"+argv[3]
	fourst_output = "fourst_"+argv[3]
	summary = "summary_"+argv[3]
	first_output_2 = "first_"+argv[3]+"_2"
	second_output_2 = "second_"+argv[3]+"_2"


	"""Construction de ma lst_of_haplo_object"""
	lst_of_haplo_object = read_input_file(haplotype, Haplotype, "\t")
	#print ("Nombre d'objet haplo :",len(lst_of_haplo_object))
	""" Construction de ma lst_of_geno_object"""
	lst_of_geno_object = read_input_file(genotype, Genotype, ",")
	#print ("Nombre d'objet geno :",len(lst_of_geno_object))

	"""Récupératoin du nombre de markers Hmz et Htz par génotype avec en plus l'index des position Htz"""
	#print ("Les marqueurs des genotypes sont {}:".format(lst_of_geno_object[1].markers))
	for geno in lst_of_geno_object :
		geno.index_htz_markers_in_seq = (geno.position_htz_markers())
		geno.nb_htz_markers = geno.have_nb_htz_markers()
		geno.nb_hmz_markers = geno.have_nb_hmz_markers()
		#print ("il a {} marqueurs Hmz et {} Htz".format(geno.nb_hmz_markers, geno.nb_htz_markers))


	#
	for geno in lst_of_geno_object :
		for haplo in lst_of_haplo_object :
			geno.select_similar_haplotype(geno, haplo) #Threshold ici si je veux récupérer plus d'haplotype similaire
			geno.number_of_similar_haplotype = len(geno.similar_haplotype)


	#écriture de la première sortie
	"""Comparaison 1 par 1 des génotype avec la liste des haplotype"""
	compare_output(first_output, lst_of_geno_object, lst_of_haplo_object)
	"""Comparaison des haplotypes les uns par rapport aux autres 
	pour pouvoir comparer leur distribution avec celle des génotypes"""
	compare_output(fourst_output, lst_of_haplo_object, lst_of_haplo_object)
	#Essayer de traité directement cette sortie pour avoir 2 autres sorties utiles pour avoir la distribution des erreurs

	"""A second output to see each similar Hmz haplotype of our Genotype in the Genotype object list"""
	compare_output_result(second_output, lst_of_geno_object)



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
		




	#écriture de la troisième sortie et récupération de la liste de nouveau haplotype
	lst_of_haplo_object_expanded = new_haplotype_output(third_output, lst_of_geno_object) 






















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

	#une autre fonction qui traite la sortie dico de ce que j'ai ci-dessus et revois ce que j'ai ci-dessous
	print ("\n\nSi 2 haplotypes similaires au géno :\n{} ne donne rien \n{} combinent et donne le génotype".format(count_2_0, count_2_1))
	print ("\n\nSi 3 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont les 3 combinaisons possible".format(count_3_0, count_3_1, count_3_2, count_3_3))
	print ("\n\nSi 4 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons".format(count_4_0, count_4_1, count_4_2))
	print ("\n\nSi 5 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison ".format(count_5_0, count_5_1))
	print ("\n\nSi 6 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont 3 combinaison ".format(count_6_0,count_6_1, count_6_2, count_6_3))











	#Sortie txt générale.
	with open(summary,'w') as txt_otp1 :
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
	lst_of_haplo_object_all = lst_of_haplo_object + lst_of_haplo_object_expanded
	
	print(len(lst_of_haplo_object))
	print(len(lst_of_haplo_object_expanded))
	print(len(lst_of_haplo_object_all))
	print(len(lst_genotype_non_confirmed))


	#Screnning step. We look if they are identical new halpotype ===> OK
	for new_haplo in lst_of_haplo_object_expanded :
		new_haplo.similar_new_haplotype = new_haplo.screening_himself(lst_of_haplo_object_expanded)
		new_haplo.number_of_similar_new_haplotype = len(new_haplo.similar_new_haplotype)

	#Filter on lst_of_haplo_object_expanded, some haplotype are the same (but not usually the same genotype and haplotype for his creation) ===> OK
	lst_of_haplo_object_expanded_filter = []
	for haplo in lst_of_haplo_object_expanded:
		if haplo.number_of_similar_new_haplotype == 0:
			lst_of_haplo_object_expanded_filter.append(haplo)
		if haplo.number_of_similar_new_haplotype > 0:
			count = 0
			for identiq_haplo in haplo.similar_new_haplotype:
				if identiq_haplo in lst_of_haplo_object_expanded_filter:
					count += 1
			if count == 0 :
				lst_of_haplo_object_expanded_filter.append(haplo)
	print("nb new haplo après filter : {}".format(len(lst_of_haplo_object_expanded_filter)))




	#Add new_haplo which are similar to our genotype no confirmed to the list of similar_haplotype
	#And change the number of similar haplotype
	with open(first_output_2, 'w') as otp1_2, open(second_output_2, 'w') as otp2_2 :
		my_otp1_2_writer = writer(otp1_2, delimiter=delimit)
		my_otp2_2_writer = writer(otp2_2, delimiter=delimit)


	#écriture de la première sortie
		for geno_non_confirmed in lst_genotype_non_confirmed :
			for new_haplo in lst_of_haplo_object_expanded_filter :
				#Repérage des new_haplo identique aux genotypes restant
				geno_non_confirmed.select_similar_haplotype(geno_non_confirmed, new_haplo)
				#Changer de nombre d'haplo similaire (faire une diff entre les deux a ce niveau?)
				geno_non_confirmed.number_of_similar_haplotype = len(geno_non_confirmed.similar_haplotype)
				#écriture ce fait ici (faire le nouveau fichier de sortie)
				my_otp1_2_writer.writerow(geno_non_confirmed.compare_two_seq(geno_non_confirmed, new_haplo))
	
		#petite vérification
		#for g in lst_genotype_non_confirmed :
		#	print("\ngeno : {} ".format(g.name))
		#	print("les haplotype sim sont :")
		#	print(g.number_of_similar_haplotype)
		#	for i in range(len(g.similar_haplotype)):
		#		print((g.similar_haplotype)[i].name)

		otp1_2.close()


	#écriture de la seconde sortie (à revoir pas clair à la lecture)
		lst_header =[]
		lst_header.append("Genotype")
		lst_header.append("Haplotype")	
		for markers in lst_genotype_non_confirmed[0].markers :
			lst_header.append(markers)
		my_otp2_2_writer.writerow(lst_header)


		for geno in lst_genotype_non_confirmed:
			geno_second_sortie = []
			geno_second_sortie.append(geno.name)
			geno_second_sortie.append(geno.number_of_similar_haplotype)
			for values in geno.sequence :
				geno_second_sortie.append(values)
			my_otp2_2_writer.writerow(geno_second_sortie)

			
			if geno.number_of_similar_haplotype > 0 :
				for similar_haplo in geno.similar_haplotype :
					haplo_second_sortie = []
					haplo_second_sortie.append(geno.name)
					haplo_second_sortie.append(similar_haplo.name)
					for values in similar_haplo.sequence :
						haplo_second_sortie.append(values)
					my_otp2_2_writer.writerow(haplo_second_sortie)
				my_otp2_2_writer.writerow("\n")
			else : 
				my_otp2_2_writer.writerow("\n")
			
		otp2_2.close()








	#Sortie shell voir comment la traiter mieux que ça
	count_geno_non_confirmed = 0
	count = 0
	for i in range((len(lst_of_haplo_object_all)+1)) :
		count_geno_non_confirmed += count
		count = 0
		for geno_non_confirmed in lst_genotype_non_confirmed :
			count += count_genotype_with_same_number_of_similar_haplotype(genotype=geno_non_confirmed, theNumber=i)
		if count_geno_non_confirmed < len(lst_genotype_non_confirmed) :		
			print ("Les genotypes avec {} haplotype(s) commun(s) sont au nombre de {}".format(i, count))



	for geno in lst_genotype_non_confirmed :
		#Parmi les haplotype similaire à notre génotype, lesquels combiné l'un avec l'autre redonne le génotype
		geno.probable_haplotypes_combinaison_2_run = geno.combinaison_between_similar_haplotype_in_geno()
		#Le nombre de combinaison obtenues ci-dessus sont possible pour notre génotype.
		geno.number_of_probable_haplotypes_combinaison_2_run = len(geno.probable_haplotypes_combinaison_2_run)
		#print("\n",geno.name)
		#print("{} similar haplo".format(geno.number_of_similar_haplotype))
		#print("have : {} combi proba".format(geno.number_of_probable_haplotypes_combinaison_2_run))



	count_2_0 = 0
	count_2_1 = 0

	count_3_0 = 0
	count_3_1 = 0
	count_3_2 = 0
	count_3_3 = 0

	count_4_0 = 0
	count_4_1 = 0
	count_4_2 = 0
	count_4_3 = 0
	count_4_4 = 0
	count_4_5 = 0
	count_4_6 = 0		

	count_5_0 = 0
	count_5_1 = 0
	count_5_2 = 0
	count_5_3 = 0
	count_5_4 = 0
	count_5_5 = 0
	count_5_6 = 0
	count_5_7 = 0
	count_5_8 = 0
	count_5_9 = 0
	count_5_10 = 0

	count_6_0 = 0
	count_6_1 = 0
	count_6_2 = 0
	count_6_3 = 0
	count_6_4 = 0
	count_6_5 = 0
	count_6_6 = 0
	count_6_7 = 0
	count_6_8 = 0
	count_6_9 = 0
	count_6_10 = 0
	count_6_11 = 0
	count_6_12 = 0
	count_6_13 = 0
	count_6_14 = 0
	count_6_15 = 0



	for geno in lst_genotype_non_confirmed :
		if geno.number_of_similar_haplotype == 2 : 
			if geno.number_of_probable_haplotypes_combinaison_2_run == 0 :
				count_2_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 1 :
				count_2_1 +=1
		
		elif geno.number_of_similar_haplotype == 3 :
			if geno.number_of_probable_haplotypes_combinaison_2_run == 0 :
				count_3_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 1 :
				count_3_1 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 2 :
				count_3_2 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 3 :
				count_3_3 += 1
		
		elif geno.number_of_similar_haplotype == 4 :
			if geno.number_of_probable_haplotypes_combinaison_2_run == 0 :
				count_4_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 1 :
				count_4_1 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 2 :
				count_4_2 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 3 :
				count_4_3 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 4 :
				count_4_4 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 5 :
				count_4_5 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 6 :
				count_4_6 += 1

		elif geno.number_of_similar_haplotype == 5 :
			if geno.number_of_probable_haplotypes_combinaison_2_run == 0 :
				count_5_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 1 :
				count_5_1 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 2 :
				count_5_2 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 3 :
				count_5_3 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 4 :
				count_5_4 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 5 :
				count_5_5 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 6 :
				count_5_6 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 7 :
				count_5_7 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 8 :
				count_5_8 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 9 :
				count_5_9 +=1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 10 :
				count_5_10 +=1

		elif geno.number_of_similar_haplotype == 6 :
			if geno.number_of_probable_haplotypes_combinaison_2_run == 0 :
				count_6_0 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 1 :
				count_6_1 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 2 :
				count_6_2 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 3 :
				count_6_3 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 4 :
				count_6_4 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 5 :
				count_6_5 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 6 :
				count_6_6 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 7 :
				count_6_7 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 8 :
				count_6_8 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 9 :
				count_6_9 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 10 :
				count_6_10 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 11:
				count_6_11 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 12:
				count_6_12 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 13:
				count_6_13 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 14:
				count_6_14 += 1
			elif geno.number_of_probable_haplotypes_combinaison_2_run == 15:
				count_6_15 += 1



	#une autre fonction qui traite la sortie dico de ce que j'ai ci-dessus et revois ce que j'ai ci-dessous
	print ("\n\nSi 2 haplotypes similaires au géno :\n{} ne donne rien \n{} combinent et donne le génotype".format(count_2_0, count_2_1))
	print ("\n\nSi 3 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont les 3 combinaisons possible".format(count_3_0, count_3_1, count_3_2, count_3_3))
	print ("\n\nSi 4 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont les 3 combinaisons \n{} ont les 4 combinaisons \n{} ont les 5 combinaisons \n{} ont les 6 combinaisons possible".format(count_4_0, count_4_1, count_4_2, count_4_3, count_4_4, count_4_5, count_4_6))
	print ("\n\nSi 5 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont 3 combinaisons \n{} ont 4 combinaisons \n{} ont 5 combinaisons \n{} ont 6 combinaisons \n{} ont 7 combinaisons \n{} ont 8 combinaisons \n{} ont 9 combinaisons \n{} ont 10 combinaisons".format(count_5_0, count_5_1, count_5_2, count_5_3, count_5_4, count_5_5, count_5_6, count_5_7, count_5_8, count_5_9, count_5_10))
	print ("\n\nSi 6 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont 3 combinaisons \n{} ont 4 combinaisons \n{} ont 5 combinaisons \n{} ont 6 combinaisons \n{} ont 7 combinaisons \n{} ont 8 combinaisons \n{} ont 9 combinaisons \n{} ont 10 combinaisons \n{} ont 11 combinaisons \n{} ont 12 combinaisons \n{} ont 13 combinaisons \n{} ont 14 combinaisons \n{} ont 15 combinaisons".format(count_6_0,count_6_1, count_6_2, count_6_3, count_6_4, count_6_5, count_6_6, count_6_7, count_6_8, count_6_9, count_6_10, count_6_11, count_6_12, count_6_13, count_6_14, count_6_15))
	c2 = count_2_0 + count_2_1
	c3 = count_3_0 + count_3_1 + count_3_2 + count_3_3
	c4 = count_4_0 + count_4_1 + count_4_2 + count_4_3 + count_4_4 + count_4_5 + count_4_6
	c5 = count_5_0 + count_5_1 + count_5_2 + count_5_3 + count_5_4 + count_5_5 + count_5_6 + count_5_7 + count_5_8 + count_5_9 + count_5_10
	c6 = count_6_0 +count_6_1 + count_6_2 + count_6_3 + count_6_4 + count_6_5 + count_6_6 + count_6_7 + count_6_8 + count_6_9 + count_6_10 + count_6_11 + count_6_12 + count_6_13 + count_6_14 + count_6_15
	print (c2,c3,c4,c5,c6)

#A partir de la il faut

	# OK #Reparcourir lst_geno_objet et créer une nouvelle liste sans les geno retrouver avec nos haplotypes (309 geno)
	#Mettre dans le fichier texte le nombre et le nom des genotypes pour lesquels les haplotypes connues permettent de les décrires
	# OK #Ajouter à la liste des haplo les nvx haplo(tous?) ---> tous ici
	#2ème run avec d'autres fichier d'output
		# OK #Avoir la nouvelle liste d'haplo similaire (add new haplo sur ceux dejà existant)
		#Sortie like la première pour le 2nd run
		#Combiner les haplo similaire (nvl list de combi permet de comparer avec la precedente)
		#Sortie like la seconde pour le 2nd run
		# ... #Faire fonction pour avoir le nombre de combinaison et tout
		#peut être faire un main avec run et ecriture d'output séparé (écriture d'output dans une fonction, comme ça 2ème run juste changer les arguments)


	fin2 = time.time()
	temps2 = fin2 - debut2
	print ("\n\n\nLe temps d'execution du second run est de : {}".format(temps2))



	
	print ("Haplo name, redondance, occurence similitude avec genotype")

	for haplo in lst_of_haplo_object_expanded:
		blabla = []
		haplo.similar_occurence = haplo.occurence_new_haplotype(lst_genotype_non_confirmed)
		blabla.append(haplo.name)
		blabla.append((haplo.number_of_similar_new_haplotype)+1)
		blabla.append(haplo.similar_occurence)
		print(blabla)

#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!#Create a READme !!!!!!!

