#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import csv
from csv import reader, writer


#Penser a mettre les commentaire en anglais



"""Program that give us SNP position if we have a new reference assembly for chicken"""


def getStrand(strd):
	"""Fonction permettant de repérer qu'elle séquence flanquante a subie le blast
	5' ou 3'.
	Information contenue par la 1er colonne du fichier de sortie du blastall
	strd row[0]"""
	return strd.rsplit("_", 1)[1]

def getSNPName(snp):
	"""Fonction permettant de retourner le SNP étudié
	strd 	row[0]"""
	return snp.rsplit("_", 1)[0]

def getAlignmentLength(taille):#Taille de l'alignement ==> rows[4]
	"""Fonction permettant de récupérer la taille de notre alignement aprés le 
	blast
	taille 	row[3]"""
	return int(taille) 
	#Depende de comment je vais parcourir mon csv (filedname ou row)
	#soit juste regarder si row[4] différent de 100 et retourner longueure
	#soit différence entre row[6] et row[7]

def getQueryPosition(strd, Qstart, Qend):
	"""Fonction permettant de retourner la position avant sur la query avant le SNP
	strd 	row[0]
	Qstart 	row[6]
	Qend 	row[7]"""
	if getStrand(strd) == "5'" :
		return int(Qend)
	else :
		return int(Qstart)

def getSbjctPosition(strd, SbjctStart, SbjctEnd): 
	"""Fonction permettant de retourner la position avant sur la sbjct avant le SNP
	strd 	row[0]
	SbjctStart 	row[8]
	SbjctEnd 	row[9]"""
	if getStrand(strd) == "5'" :
		return int(SbjctEnd)
	else :
		return int(SbjctStart)

def getMissingPiecesLength(strd, Qstart, Qend):
	"""Fonction permettant de retourner la taille manquante jusqu'au SNP
	strd 	row[0]
	Qstart 	row[6]
	Qend 	row[7]"""
	if getStrand(strd) == "5'" and getQueryPosition(strd, Qstart, Qend) != 100 :
		return (100 - getQueryPosition(strd, Qstart, Qend) +1)
	elif getStrand(strd) == "3'" and getQueryPosition(strd, Qstart, Qend) != 1 :
		return (getQueryPosition(strd, Qstart, Qend))
	else:
		return 1

def getSbjctOrientation(SbjctStart, SbjctEnd):
	"""Fonction permettant de repérer le sens de la séquence subject
	True si sbjct start < sbjct end (sens identique à la séquence query)
	et False si inversement (sens inverse à la séquence query)
	SbjctStart 	row[8]
	SbjctEnd 	row[9]"""
	if int(SbjctStart) < int(SbjctEnd) :
		return True
	else:
		return False

def getEValue(evalue):
	"""Fonction permettant de retourner la valeur de la e-value de l'alignement
	permet sélection du meilleur alignement pour une même séquence
	e-value 	row[10]"""
	return float(evalue)
	#Avoir un commentaire quand c'est le cas.

def getSNPPositin(strd, Qstart, Qend, SbjctStart, SbjctEnd):
	"""Fonction permettant de récupérer la position du SNP dans l'assemblage
	à partir de la position de la sbjct
	strd 	row[0]
	Qstart 	row[6]
	Qend 	row[7]
	SbjctStart 	row[8]
	SbjctEnd 	row[9]"""
	if getStrand(strd) == "5'" and getSbjctOrientation(SbjctStart, SbjctEnd) == True :
		return getSbjctPosition(strd, SbjctStart, SbjctEnd) + getMissingPiecesLength(strd, Qstart, Qend)
	elif getStrand(strd) == "5'" and getSbjctOrientation(SbjctStart, SbjctEnd) == False :
		return getSbjctPosition(strd, SbjctStart, SbjctEnd) - getMissingPiecesLength(strd, Qstart, Qend)
	elif getStrand(strd) == "3'" and getSbjctOrientation(SbjctStart, SbjctEnd) == True :
		return getSbjctPosition(strd, SbjctStart, SbjctEnd) - getMissingPiecesLength(strd, Qstart, Qend)
	elif getStrand(strd) == "3'" and getSbjctOrientation(SbjctStart, SbjctEnd) == False :
		return getSbjctPosition(strd, SbjctStart, SbjctEnd) + getMissingPiecesLength(strd, Qstart, Qend)
	#necesite peut-être fonction qui récupére info des colonnes 8 et 9 (avec fonction précédente)
	#puis calcule des positions
	#Ne pas oublier ici condition du strand (5 ou 3)

def comparePosition():
	"""Une comparaison entre la position obtenue avec la séquence flanquante en 3'
	et la séquence flanquante en 5'"""
	if infoList5[0] == infoList3[0] and infoList5[1] == "5'" and infoList3[1] == "3'" :
		if infoList5[3] == infoList3[3] :
			#print("Même position trouvé avec les 2 séquences flanquantes ;) bien joué")
			return infoList3[3]
		else :
			#print ("Il y a un problème dans tes calculs de position ou comparaison de listes")
			return "NA"
	else :
		pass
	#vérifier si 1 position dans 2 listes différentes sont les même ou pas.
	#soit vérifier si = 
	#soit vérifier si la soustraction =0

def getComment():
	"""Fonction permettant d'avoir un retour sur l'alignement
	Est-ce qu'il y a plusieur alignement sous notre seuil de e-value?
	Si le pourcentage d'identité n'est pas de 100, retourner le pourquoi
	Si l'alignement observer n'est pas de la longueur de la query introduit"""
	return "#######"
	#retourne une liste de commentaires




infoList =list() #sert a vérifier la e-value (si plusieurs alignement pour 1 séquence) avec le résultat précédent




if __name__ == '__main__':
	intp = argv[1]
	outp = argv[2]
	delimit = "\t"
	infoList5 = list()
	infoList3 = list()
	infoListOutput = list()
	#infoList, infoList3 and infoList5 structure --> [SNPname, 5' or 3', position find, %id, e-value comment]
	#infoList, allows comparison of the e-value if multiple alignment returned by the blast
	#infoListOutput --> [SNPname, final position find, comments]
	with open(intp, 'r') as src, open(outp, 'w') as otp :
		my_reader = reader(src, delimiter = delimit)
		my_writer = writer(otp, delimiter = "\t")
		count = 0
		for rows in my_reader :
			infoList = list()
			count += 1
			infoList.append(getSNPName(rows[0]))
			infoList.append(getStrand(rows[0]))
			infoList.append(getEValue(rows[10]))
			infoList.append(getSNPPositin(rows[0], rows[6], rows[7], rows[8], rows[9]))
			print "\n"
			print count, "##################", infoList

			#Si pas d'info dans infoList3 ou 5 je remplie avec celle que j'ai pour cette ligne
			if infoList[1] == "3'" and infoList3 == [] :
				infoList3 = infoList
				print "La liste d'info 3 concervée est : ",  infoList3
			else :
				pass
			
			if infoList[1] == "5'" and infoList5 == [] :
				infoList5 = infoList
				print "La liste d'info 5 concervée est : ",  infoList5
			else :
				pass



			#Si plusieurs alignements pour la même séquence (5')
			#Ou si changement de SNP
			if infoList5 != [] and infoList[0] == infoList5[0] :
				if infoList[1] == infoList5[1] and infoList[2] < infoList5[2] :
					infoList5 = infoList
					print "Chagement de référence pour cet alignement : ",  infoList5
				else :
					pass
			else :
				#faire la comparaison ici?
				infoList5 = infoList
				print "Pas le même SNP"
				print "La liste d'info 3 concervée est : ", infoList5
				
			#Si plusieurs alignements pour la même séquence (3')
			#Ou si changement de SNP
			if infoList3 != [] and infoList[0] == infoList3[0] :
				if infoList[1] == infoList3[1] and infoList[2] < infoList3[2] :
					infoList3 = infoList
					print "Chagement de référence pour cet alignement: ",  infoList3
				else :
					pass
			else :
				#faire la comparaison ici? 
				infoList3 = infoList
				print "pas le même SNP"
				print "La liste d'info 3 concervée est : ", infoList3






"""
			
			#gérer 
			if infoList[0] == infoList5[0] :
				if infoList[1] == infoList5[1] and infoList[2] < infoList5[2] :
					infoList5 = infoList
					print count, infoList5
				elif infoList[1] == infoList3[1] and infoList[2] < infoList3[2] :
					infoList3 = infoList
				else : 
					pass
			elif infoList[0] == infoList5[0] and infoList[1] == "3'" :
				infoList3 = infoList
								
			

			#Attention il faut avoir infoList5 et 3 rempli (si 1 vide index ouit of range)
			#Attention gérer le faite que l'on peut avoir que infoList5 ou 3 pour un SNP donnée						
			if infoList5[0] == infoList3[0] :
				infoListOutput.append(infoList3[0])
				infoListOutput.append(comparePosition())
				infoListOutput.append(getComment())
				my_writer.writerow(infoListOutput)
				infoListOutput = list()"""