#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Récupérer le génotype de référence gg4 (Ensembl) et gg5 (NCBI) et celui de Shiina AB268588
#Avec les positions fraichement récupérées avec le blast.


import requests, sys
from sys import argv
from csv import reader, writer

 
#bouclé sur chaque coordonnée du fichier
#retourner les résultats dans un string et l'écrire autre part
intp = argv[1]
#outp = argv[2]
delimit = "\t"
sequence = str()
with open(intp, 'r') as src : #, open(outp, 'w') as otp :
		my_reader = reader(src, delimiter = delimit)
		#my_writer = writer(otp, delimiter = '|')
		count = 0
		for rows in my_reader :
			count += 1
			server = "http://rest.ensembl.org"
			ext = "/sequence/region/chicken/16:"+rows[0]+".."+rows[0]+"?"
			#print (ext)
			r = requests.get(server + ext, headers={ "Content-Type" : "text/plain"})
			
			if not r.ok :
				r.raise_for_status()
				sys.exit
		
			sequence = sequence + r.text
			#print (sequence)
			#print (len(sequence))
		print (sequence)
		#print ("fini")
		#my_writer.writerow(sequence)








"""
server = "http://rest.ensembl.org"
ext = "/sequence/region/chicken/16:221162..221162:-1?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
 
print (r.text)
"""
