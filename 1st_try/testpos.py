#!/usr/bin/env python

import csv
import sys
import time
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

prout = open("my_blast_all.xml")
blast_records = NCBIXML.read(prout)
print blast_records

"""
#je lui donne en argument le fichier?
def getBlastInfo ():
	save_file = open("my_blast_all.xml")
	#Si qu'une sequence blast il suffi de faier un .read
	#blast.record = NCBIXML.read(save_file)
	#Sinon utiliser une for-loop avec un .parse
	blast.record = NCBIXML.parse(save_file)
	for blast_record in blast_records:
		#iterations sur le nombre de blast effectue
		for alignment in blast_record.alignments:
			for hsp in alignment.hsps:
				if hsp.expect < 0.04:
					#des print pour le moment
					#remplissag de nouveau dico ensuite
					print('*****Alignement*****')
					print('sequence :' alignment.title)
					print('taille alignement :' alignment.length)
					print('e-value :' hsp.expect)
					print('strand :' hsp.strand)
					print('debut query:' hsp.query_start)
					print('fin query:' hsp.query_end)
					print('debut sbjct:' hsp.sbjct_start)
					print('fin sbjct:' hsp.sbjct_end)
					print(hsp.query[0:alignment.length])
					print(hsp.match[0:alignment.length])
					print(hsp.sbjct[0:alignment.length])

"""