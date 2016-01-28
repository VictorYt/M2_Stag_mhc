#!/usr/bin/env python

import csv
import sys

#recuperation des colonnes d'interet
with open(sys.argv[1],"rb") as csvfileEntree:
	cE = csv.reader(csvfileEntree, delimiter = '\t', quotechar = '|')
	for row in cE:
		dico1[row[0]]= row[1]
		dico2[row[0]]= row[]


#reecriture dans un autres csv
with open(sys.argv[2],"rb") as csvfileSortie:
	cS = csv.write(csvfileSortie, delimiter = ' ', quotechar = '|')


#travailler ça ce soir