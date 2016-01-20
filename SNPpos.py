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
		#attention dico ne concerve pas l'ordre de la liste du .csv


def getHelp():
	"""Fonction d'aide"""
	#a elaborer une fois fini
	pass


######################
##########Obtention de la position du SNP dans genome de ref (galGal4 puis galGal5)
######################

#A faire
#OK <== regarder comment prendre qu'une partie de la sequence. av [.../...]
#OK <== regarder pour faire la meme chose avec les 2 sequences de references NC_006103.3 et .4
	#marche pas avec .3 (gg4)
#regarder si on peut avoir la taille de la querry a la sortie
	#normalement de la meme taille qu'a l'entree
#regarder le brin plus ou minus du sbject
#faire loperation +n ou -n pour obtenir la position exacte
#ajout de commentaire auto
#ajout de la position dans le dico en fonction de la querry utilisee
#creer les fichiers de sorties



#Boucler avec les 96 SNP
	#faire une fonction pour selectionner juste la seq flanquante gauche ou droite
def getSeqFlan5(n):
	"""Permet de recuperer la sequence flanquante en 5' d'un SNP
	n est la position dans le dictionnaire du SNP"""
	return dicoSNP.get(dicoSNP.keys()[n])[0:100]
	#[0:100]
	#Attention la taille des seq flanquante peut etre diff de 100
	#trouver moyen de l'arreter avant [


def getSeqFlan3(n):
	"""Permet de recuperer la sequence flanquante en 3' d'un SNP
	n est la position dans le dictionnaire du SNP"""
	return dicoSNP.get(dicoSNP.keys()[n])[105:205]
	#[105:205]
	#Attention la taille des seq flanquante peut etre diff de 100
	#trouver moyen de le demarrer apres ]


#verification du fonctionnement des 2 fonctions ci-dessus
for cle, valeur in dicoSNP.items():
	print ("La clef {} contient la valeur 5' {} et la valeur 3' {}.".format(cle, getSeqFlan5(dicoSNP.keys().index(cle)), getSeqFlan3(dicoSNP.keys().index(cle))))


def makeBlast():
	"""La fonction makeBlast effectue un blast des sequences flanquantes des SNP contre NC_006103.4 
	...
	...
	...

	"""
	debut1=time.time()
	save_file = open("my_blast_all", "w")
	for cle, valeur in dicoSNP.items():
		print "lance blast {} du {}:".format(dicoSNP.keys().index(cle), cle)
		debut = time.time()
		result_handle= NCBIWWW.qblast("blastn", "refseq_genomic",sequence="{}".format(getSeqFlan5(dicoSNP.keys().index(cle))), entrez_query="NC_006103.4[RefSeq]", format_type='Text')
		print "blast fini \t"
		fin = time.time()
		print "il a mis :", fin-debut
		save_file.write(result_handle.read())
		save_file.write("\n\n\n\t\t\t ###################Alignement suivant###################  \n\n\n")
	fin1=time.time()
	print "le temps total est de :", fin1-debut1
	save_file.close()
#Voir pour faire la boucle sur le dicoSNP hors de la fonction




#fichier de sortie de l alignement (format text)
#reste a choisir 
	#le bon alignement (avec la e-value la plus basse)
	#le strand (savoir si plus ou moins pour retrouver la position du SNP)
	#la position du SNP en fonction de la sequence flanquante (5' ou 3')




def getPos5():
	"""Recupere la position pour sequence flanquante 5'"""
	pass

def getPos3():
	"""Idem mais avec la sequence flanquante 3'"""
	pass




def getNewSNPpos ():
	"""Genere les dictionnaires avec les nouvelles positions de SNP dans

	"""
	pass



def CompareGetPos():
	"""Permet de comparer les positions des SNP, recuperer avec les 2 sequences flanquantes
	Si =0 meme position trouvee"""
	pass
























"""
#methode de recuperation des donnees

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

























######################
#Ecriture des fichier de sortie
######################
"""
#Argv[3]=nom que l'on souhaite pour le fichier de sortie
with open(argv[3], 'wb') as csvfileSortie:
	crS = csv.writer(csvfileSortie, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	crS.writerow()
"""









