#!/usr/bin/env python

import csv
import sys
import time
from Bio.Blast import NCBIWWW

#variables
dicoSNP = {}


#remplissage dicoSNP
#Lecture du fichier d'entree (.csv)
	# argument 1 = "Markers_position_16_Shiina.csv"
with open(sys.argv[1],"rb") as csvfileEntree:
	cr = csv.reader(csvfileEntree, delimiter = '\t', quotechar = '|')
	#creation dico clef = SNPname, valeur = sequence
	for row in cr:
		dicoSNP[row[0]]= row[1]
	#print dicoSNP
		#attention pas le meme ordre que dans table csv


def getSeqFlan5(n):
	return dicoSNP.get(dicoSNP.keys()[n])[0:100]


def getSeqFlan3(n):
	return dicoSNP.get(dicoSNP.keys()[n])[105:205]


def makeBlast():
	debut1=time.time()
	save_file = open("my_blast_all", "w")
	for cle, valeur in dicoSNP.items():
		print "lance blast {} du {}:".format(dicoSNP.keys().index(cle), cle)
		debut = time.time()
		result_handle= NCBIWWW.qblast("blastn", "refseq_genomic",sequence="{}".format(getSeqFlan5(dicoSNP.keys().index(cle))), entrez_query="NC_006103.4[RefSeq]", format_type='Text')
		print "blast fini \t"
		fin = time.time()
		print "il a mis :", fin-debut
		#save_file = open("my_blast", "w")#pb j'ecrit un fichier a chaque fois / but : mettre tout dans le meme 
		save_file.write(result_handle.read())
		save_file.write("\n\n\n\t\t\t ###################Alignement suivant###################  \n\n\n")
		#save_file.close()
	fin1=time.time()
	print "le temps total est de :", debut1-fin1
	save_file.close()



makeBlast()