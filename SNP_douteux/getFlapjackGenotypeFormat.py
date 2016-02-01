#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sys import argv
from csv import reader, writer
import re


"""Script pour passer plus vite au format génotype de flapjack.
Convertie AA --> A ... et les AG en A/G ... et le reste le retranscript 
comme dans le fichier d'origine"""

transform_dico = {'AA':'A', 'CC':'C', 'GG':'G', 'TT':'T', 'AG':'A/G', 'AC':'A/C', 'AT':'A/T', 'CG':'C/G', 'TC':'T/C', 'TG':'T/G'}

def TransformeInput(inpt, outp, delimit = "\t"):
	"""Transformation du fichier tabulé en un autre fichier tabulé compatible flapjack"""
	with open(inpt, 'r') as src, open(outp, 'w') as otp :
		my_reader = reader(src, delimiter = delimit)
		my_writer = writer(otp, delimiter = "\t")
		for rows in my_reader :
			re.sub(r'AA', 'A', rows)
"""			for column in rows :
				if column in transform_dico :
					#print(transform_dico[column])
					my_writer.writerow(transform_dico[column])
				else :
					#print(column)
					my_writer.writerow(column)"""


if __name__ == '__main__':
	""" tabulation delimiteur par defaut mais possibilité de le spécifier si ce n'est pas le cas"""
	if len(argv) == 3:
		TransformeInput(argv[1],argv[2])
	elif len(argv) == 4:
		TransformeInput(argv[1],argv[2], argv[3])
	else:
		print("C\'est faux")
	print("Terminé")


#Voir ce qui merde 