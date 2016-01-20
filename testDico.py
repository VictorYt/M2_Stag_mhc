#!/usr/bin/env python

import csv
import sys

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



#fonction qui recupere la meme chose
for cle, valeur in dicoSNP.items():
	print ("La clef {} contient la valeur 5' {} et la valeur 3' {}.".format(cle, getSeqFlan5(dicoSNP.keys().index(cle)), getSeqFlan3(dicoSNP.keys().index(cle))))