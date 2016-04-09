#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sys import argv
from csv import reader, writer
from Bio import SeqIO

#pour faire ce que je veux http://sequenceconversion.bugaco.com/converter/biology/sequences/tab_to_fasta.php
#mais pas de découpage des seq flanquante
#pour faire l'inverse de ce que je veux http://darwin.biochem.okstate.edu/fasta2tab/

"""Programme permettant de passer d'un format texte (.csv) à 2 colonnes (SNP_ID/Sequences)
à un multi-format fasta qui contient pour chaque SNP les 2 séquences flanquantes seules"""




def getSeqFlanq5(seq):
	"""n la séquence avec les 2 sequences flanquantes et le polymorphuisme [A/B]
	getSeqFlanq5 renvoie le string avant le caractère '[' """
	return seq.rsplit("[", 1)[0]

def getSeqFlanq3(seq):
	"""seq la séquence avec les 2 sequences flanquantes et le polymorphuisme [A/B]
	getSeqFlanq5 renvoie le string après le caractère '[' """
	return seq.rsplit("]", 1)[1]


def TransformeInput(inpt, outp, delimit = "\t"):
	"""Transformation du fichier tabulé en un autre fichier tabulé dans lequel
	la sequence est coupé par sequences flanquantes"""
	with open(inpt, 'rb') as src, open(outp, 'wb') as otp:
		my_reader = reader(src, delimiter = delimit)
		my_writer = writer(otp, delimiter = "\t")
		for rows in my_reader :
			my_writer.writerow(("%s_5'" %(rows[0]), getSeqFlanq5(rows[1])))
			my_writer.writerow(("%s_3'" %(rows[0]), getSeqFlanq3(rows[1])))





if __name__ == '__main__':
	""" tabulation delimiteur par defaut mais possibilité de le spécifier si ce n'est pas le cas"""
	if len(argv) == 3:
		TransformeInput(argv[1],argv[2])
		RealTransforme = SeqIO.convert(argv[2], "tab", "multi_maker.fasta","fasta")
	elif len(argv) == 4:
		TransformeInput(argv[1],argv[2], argv[3])
		RealTransforme = SeqIO.convert(argv[2], "tab", "multi_maker.fasta","fasta")
	else:
		print("C\'est faux")
	print("Terminé")


#custumisation
	#gérer les input (pas normal que l'on donne le nom de l'intermédiaire et pas le final)
	#gérer l'odre des arguments (styme -i -o -d -f(lui trouver une lettre qui convient))
	# faire les 2 blast
		#blastall -i
		#
	#gérer la sortie (Taille query/taille sbjct/sens sbjct/Comparaison 5' et 3'/Commentaire a chaque étape)
