#!/usr/bin/env python

import csv 
import sys
import time
from Bio import pairwise2 #pas utilise
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML #pas encore ultilise


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
	print dicoSNP
		#attention pas le meme ordre que dans table csv


######################
##########Obtention de la position du SNP dans genome de ref (galGal4 puis galGal5)
######################

#A faire
#regarder comment prendre qu'une partie de la sequence. av [.../...]
#regarder pour faire la meme chose avec les 2 sequences de references NC_006103.3 et .4
#regarder si on peut avoir la taille de la querry a la sortie
#regarder le brin plus ou minus du sbject
#faire loperation +n ou -n pour obtenir la position exacte
#ajout de commentaire auto
#ajout de la position dans le dico en fonction de la querry utilisee
#creer les fichiers de sorties



#Boucler avec les 96 SNP
	#faire une fonction pour selectionner juste la seq flanquante gauche ou droite

#trop long (11min/seq) mais marche avec la derniere version dassemblage
#fichier de sortie de l alignement
#reste a choisir 
	#le bon alignement
	#la position du SNP en fonction de la sequence flanquante choisie
print "lance blast :"
debut = time.time()
result_handle = NCBIWWW.qblast("blastn", "refseq_genomic",sequence="TTGGGTGTTTTGACCCAAAACCTATTCATGGTGAAGACACCTTTGGAGGAACTGATGCAGTCGGGTGGGGACACACAGAGGGATTCACCCCACATTTCCC", entrez_query="NC_006103.3[RefSeq]", format_type='Text')
#(plus lente)result_handle = NCBIWWW.qblast("blastn", "refseq_genomic",sequence="TTGGGTGTTTTGACCCAAAACCTATTCATGGTGAAGACACCTTTGGAGGAACTGATGCAGTCGGGTGGGGACACACAGAGGGATTCACCCCACATTTCCC", entrez_query="GCF_000002315.4[assembly]", format_type='Text')
print "blast fini \t"
fin = time.time()
print "il a mis :", fin-debut
save_file = open("my_blast", "w")
print "write in .txt file"
save_file.write(result_handle.read())
save_file.close()

""" c est nul ce truc/marche pas
result_handle.close()
result_handle = open("my_blast.xml")
records = NCBIXML.parse(result_handle)
blast_record = records.next()
for alignment in blast_record.alignments:
	for hsp in alignment.hsps:
		if hsp.expect <0.01:
			print ('*****Alignement*****')
			print "sequence:"alignment.title
			print "length:"alignment.length
			print "e value:"hsp.expect
			print "strand :"hsp.strand
			print "position : "
			print (hsp.query[0:len(hsp.query)] + '....')
			print (hsp.match[0:len(hsp.query)] + '....')
			print (hsp.sbjst[0:len(hsp.query)] + '....')
"""



















"""
#Avec la commande pairewise2 de biopython

#test N1
def alignementSeq(dicoRef, dicoSNP):
	for seq_ref in dicoRef.value() :
		for seq_SNP in dicoSNP.value :
			alignments = pairwise2.align.globalxx("TTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGATTGGGTGTTTTGA", "TTGGGTGTTTTGACCCAAAACCTATTCATGGTGAAGACACCTTTGGAGGAACTGATGCAGTCGGGTGGGGACACACAGAGGGATTCACCCCACATTTCCC")
	return alignments
	#faire en sorte qu'il me boucle sur les bonnes sequences, face mes fichiers de sortie

#test N2
#marche pas (KeyError)
#surrement pas cette fonction ????
for seq_SNP in  dicoSNP.values():
	alignments = pairwise2.align.globalxx("ACCGT", dicoSNP[seq_SNP])	
	print alignments
		#for a in alignments:
		#print format_alignnment(*a)

#Ce n'est pas la solution
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









