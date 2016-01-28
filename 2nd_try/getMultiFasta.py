#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Transforamtion d'un fichier text (.csv, sep={tabulation}) en fichier multi-fasta
Voir http://biopython.org/wiki/SeqIO#Sequence_Output
Pour savoir qu'elle format d'input est géré par Bio.SeqIO


Attention le fichier de sortie contient, en plus des deux séquences flanquantes le ploymorphisme entre corchet [A/B]"""

from sys import argv
from csv import reader, writer
from Bio import SeqIO


 
 
def fonction(source, outp, delimit= "\t"):
	"""Transformation du fichier tabulé en iput vers un fichier multi-fasta """
	with open(source, 'rb') as src, open(outp, 'wb') as otp:
		my_reader = reader(src, delimiter = delimit)
		#pas de csv en sortie mais un .fasta pas ça
		my_writer = writer(otp, delimiter = "\n")
		liste = list()

		for column in zip(*my_reader):
			n = 10
			liste.append(n)
		my_writer.writerows(liste)

		#plutôt comme ça en utlisant biopython
		sequence = #change alternativement entre SNP seqflanq5/seqflanq3
		my_writer = SeqIO.write(sequence, otp, "fasta")


def getSeqFlanq5():
	"""Permet de récupérer la séquence flanquante de gauche avant le polymorphisme marqué par [A/B]"""
	pass

def getSeqFlanq3():
	"""Permet de récupérer la séquence flanquante de droite après le polymorphisme marqué par [A/B]"""
	pass



if __name__ == '__main__':
	if len(argv) == 3:
		fonction(argv[1], argv[2])
	elif len(argv) == 4:
		fonction(argv[1], argv[2], argv[3])
	else:
		print("C\'est faux")
	print("Terminé")
