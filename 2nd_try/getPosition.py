#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv


#Penser a mettre les commentaire en anglais

#Variables (listes ou dico?) pour comparer position retrouvée entre les 2 séquences flanquante
# Dans les listes :
	#[SNPname, 5' or 3', position find, comment]
infoList5 = list()
infoList3 = list()


"""Program that give us SNP position if we have a new reference assembly for chicken"""


def getStrand():
	"""Fonction permettant de repérer qu'elle séquence flanquante a subie le blast
	5' ou 3'.
	Information contenue par la 1er colonne du fichier de sortie du blastall
	row[0]"""
	return row[0].rsplit("_", 1)[1]

def getSNPName():
	"""Fonction permettant de retourner le SNP étudié"""
	return row[0].rsplit("_", 1)[0]

def getAlignmentLength():#Taille de la query ou de l'alignement?
	"""Fonction permettant de récupérer la taille de notre alignement aprés le blast"""
	return int(row[4]) 
	#Depende de comment je vais parcourir mon csv (filedname ou row)
	#soit juste regarder si row[4] différent de 100 et retourner longueure
	#soit différence entre row[6] et row[7]

def getMissingPiecesLength():
	"""Fonction permettant de retourner la taille manquante jusqu'au SNP"""
	if getStrand() == "5'" and getQueryPosition() != 100 :
		return (100 - getQueryPosition() +1)
	elif getStrand() == "3'" and getQueryPosition() != 1 :
		return (getQueryPosition())
	else:
		return 1

def getSbjctOrientation():
	"""Fonction permettant de repérer le sens de la séquence subject
	True si sbjct start < sbjct end (sens identique à la séquence query)
	et False si inversement (sens inverse à la séquence query)"""
	if int(row[8]) < int(row[9]) :
		return True
	else:
		return False 

def getSbjctPosition(): 
	"""Fonction permettant de retourner la position avant sur la sbjct avant le SNP
	start row[8]
	end row[9]"""
	if getStrand() == "5'" :
		return int(row[9])
	else :
		return int(row[8])

def getQueryPosition():
	"""Fonction permettant de retourner la position avant sur la query avant le SNP
	start row[6]
	end row[7]"""
	if getStrand() == "5'" :
		return int(row[7])
	else :
		return int(row[6])


def getEValue():
	"""Fonction permettant de retourner la valeur de la e-value de l'alignement
	permet sélection du meilleur alignement pour une même séquence"""
	return float(row[10])
	#Avoir un commentaire quand c'est le cas.

def getSNPPositin():
	"""Fonction permettant de récupérer la position du SNP dans l'assemblage
	à partir de la position de la sbjct"""
	if getStrand() == "5'" and getSbjctOrientation == True :
		return getSbjctPosition() + getMissingPiecesLength()
	elif getStrand() == "5'" and getSbjctOrientation == False :
		return getSbjctPosition() - getMissingPiecesLength()
	elif getStrand() == "3'" and getSbjctOrientation == True :
		return getSbjctPosition() - getMissingPiecesLength()
	elif getStrand() == "3'" and getSbjctOrientation == False :
		return getSbjctPosition() + getMissingPiecesLength()
	#necesite peut-être fonction qui récupére info des colonnes 8 et 9 (avec fonction précédente)
	#puis calcule des positions
	#Ne pas oublier ici condition du strand (5 ou 3)

def comparePosition():
	"""Une comparaison entre la position obtenue avec la séquence flanquante en 3'
	et la séquence flanquante en 5'"""
	if infoList5[0] == infoList3[0] and infoList5[1] == "5'" and infoList3[1] == "3'" :
		if infoList5[2] == infoList3[2] :
			print("Même position trouvé avec les 2 séquences flanquantes ;) bien joué")
		else :
			print ("Il y a un problème dans tes calculs de position ou comparaison de listes")
	
	
	#vérifier si 1 position dans 2 listes différentes sont les même ou pas.
	#soit vérifier si = 
	#soit vérifier si la soustraction =0

def getComment():
	"""Fonction permettant d'avoir un retour sur l'alignement
	Est-ce qu'il y a plusieur alignement sous notre seuil de e-value?
	Si le pourcentage d'identité n'est pas de 100, retourner le pourquoi
	Si l'alignement observer n'est pas de la longueur de la query introduit"""
	pass
	#retourne une liste de commentaires



if __name__ == '__main__':
	with open(argv[1], 'r') as src, open(argv[2], 'w') as otp :
		my_reader = reader(src, delimiter = delimit)
		my_writer = writer(otp, delimiter = "\t")
		for rows in my_reader :
			#ici je rempli une liste en fonction de la strand 5 ou 3
			#je compare les 2 positions trouvée
			#print InfoList


#Ne pas oublier de comparer le nom des séquences
	# et si même nom (row[0] identique, faire une comparaison des e-values et sélectionner la plus basse)
	# attention est ce que la séquence flanquante 3' correspondante est également la séquence avec la e-value la plus basse
	#Si c'est pas le cas la comparaison des positions sera toujours fausse.
			
#mettre ici le déroulement du programme
#1 utilisation de getStrand
#2 remplisage d'une liste avec les valeurs que je veux
