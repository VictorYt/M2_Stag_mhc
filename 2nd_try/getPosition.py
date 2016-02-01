#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv



"""Programme permettant de récupérer les positions des SNP si changement 
d'assemblage de référence"""


def getStrand():
	"""Fonction permettant de repérer qu'elle séquence flanquante a subie le blast
	5' ou 3'.
	Information contenue par la 1er colonne du fichier de sortie du blastall
	row[0]"""
	pass
	#utilisation d'un parseur surement

def getQueryLength():
	"""Fonction permettant de récupérer la taille de notre query aprés le blast"""
	return row[4]
	#soit juste regarder si row[4] différent de 100 et retourner longueure
	#soit différence entre row[6] et row[7]

def getQueryMissingPieces():
	"""Fonction permettant de retourner la partie de la query manquante
	start row[6]
	end row[7]
	ou les deux"""
	pass

def getSbjctMissingPieces():
	"""Fonction permettant de retourner la partie de la séquence sbjct manquante
	start row[8]
	end row[9]
	ou les deux"""
	pass

def getPositin():
	"""Fonction permettant de récupérer la position du SNP dans l'assemblage
	à partir de la position de la sbjct
	start si on travail la séquence 3' --> row[8]
	end si on travail avec la ésquence 5' --> row[9]"""
	pass
	#necesite peut-être fonction qui récupére info des colonnes 8 et 9 (avec fonction précédente)
	#puis calcule des positions
	#Ne pas oublier ici condition du strand (5 ou 3)

def comparePosition():
	"""Une comparaison entre la position obtenue avec la séquence flanquante en 3'
	et la séquence flanquante en 5'"""
	pass
	#soit vérifier si = 
	#soit vérifier si la soustraction =0



if __name__ == '__main__':
#mettre ici le déroulement du programme
#1 utilisation de getStrand
#2 vérifier taille de la query
	#si 100 : +1 ou -1
	#si différent de 100 +ou- la différence ATTENTION dépend du Strand
#3 vérifier la taille de la sbjct
	#si = séquence query --> ok
	#si différent --> indication du problème
#4 Récuération des positions ou comparaison
#5 Comparaison des position
	#Si = pas de soucis
	#Si différentes indixation du problème
