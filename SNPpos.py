#!/usr/bin/env python

import csv 
import sys
from Bio import pairwise2
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


#Variables
dicoSNP = {}
PosSNPgg4 = {}
PosSNPgg5 = {}

######################
##########Creation du dicto contenant toutes les sequences de SNP(96)
######################
#Lecture du fichier d'entree (.csv)
	# argument 1 = "Markers_position_16_Shiina.csv"
with open(sys.argv[1],"rb") as csvfileEntree:
	cr = csv.reader(csvfileEntree, delimiter = '\t', quotechar = '|')
	#creation dico clef = SNPname, valeur = sequence
	for row in cr:
		dicoSNP[row[0]]= row[1]
	#print dicoSNP
		#attention pas le meme ordre que dans table csv


######################
##########Obtention de la position du SNP dans genome de ref (galGal4 puis galGal5)
######################
#marche pas
for seq_SNP in  dicoSNP.values():
	alignments = pairwise2.align.globalxx("ACCGT", dicoSNP[seq_SNP])	
	print alignments
		#for a in alignments:
		#print format_alignnment(*a)


"""
#Avec la commande pairewise2 de biopython
def alignementSeq(dicoRef, dicoSNP):
	for seq_ref in dicoRef.value() :
		for seq_SNP in dicoSNP.value :
			alignments = pairwise2.align.globalxx("TTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGA", "TTGGGTGTTTTGACCCAAAACCTATTCATGGTGAAGACACCTTTGGAGGAACTGATGCAGTCGGGTGGGGACACACAGAGGGATTCACCCCACATTTCCC")
	return alignments
	#faire en sorte qu'il me boucle sur les bonnes sequences, face mes fichiers de sortie
"""

"""
#Avec la commande qblast de biopython
result_handle = NCBIWWW.qblast("blastn", "nt", "TTGGGTGTTTTGACCCAAAACCTATTCATGGTGAAGACACCTTTGGAGGAACTGATGCAGTCGGGTGGGGACACACAGAGGGATTCACCCCACATTTCCC")
save_file = open("my_blast.xml", "w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
result_handle = open("my_blast.xml")
records = NCBIXML.parse(result_handle)
blast_record = records.next()
for alignment in blast_record.alignments:
	for hsp in alignment.hsps:
		if hsp.expect <0.01:
			print ('*****Alignement*****')
			print ('sequence:'alignment.title)
			print ('length:'alignment.length)
			print ('gaps:'hsp.score)
			print ('e value:'hsp.expect)
			print ('strand :'hsp.strand)
			print (hsp.query[0:len(hsp.query)] + '....')
			print (hsp.match[0:len(hsp.query)] + '....')
			print (hsp.sbjst[0:len(hsp.query)] + '....')
#Pb = Possible mais commande supplementaire pour choisir l'alignement avec les sequences de references que je souhaite CM000108.3 et.4
"""
"""
#Marche mais ne me donne pas d'alignement avec la sequence de ref que je souhaite
result_handle = NCBIWWW.qblast("blastn", "nt", "TTGGGTGTTTTGACCCAAAACCTATTCATGGTGAAGACACCTTTGGAGGAACTGATGCAGTCGGGTGGGGACACACAGAGGGATTCACCCCACATTTCCC")
save_file = open("my_blast.xml", "w")
save_file.write(result_handle.read())
save_file.close()
"""

######################
#Ecriture des fichier de sortie
######################
"""
#Argv[3]=nom que l'on souhaite pour le fichier de sortie
with open(argv[3], 'wb') as csvfileSortie:
	crS = csv.writer(csvfileSortie, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	crS.writerow()
"""