#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


#pour fenêtre glissante
#from collections import deque
#pour parcour par morceaux
#from itertools import chain, islice


import collections as co
import itertools as it
import csv
from HaplotypeR import Haplotype

# Voila les outils 
#maintenant trouve un moyen de le faire avec une liste d'haplotype donnée en entrée.

def windows(iterable, size):
	"""Fonction permettant la découpe de mes haplotypes en sous séquences"""
	iterable = iter(iterable)
	d = co.deque(it.islice(iterable, size), size)
	yield d
	for x in iterable :
		d.append(x)
		yield d


#leecture du fichier
def read_input_file(filename, objecttype, delimit):
	"""Return a list of objet by reading your input file,
	the type is determine by the argument "objecttype"

	Named parameter :
	-file -- Your input file
	-objecttype -- The type of objects you want by reading the file
	-delimit -- The delimiter of our file

	"""
	lst_of_objects = []
	with open(filename, 'r') as src :
		my_reader = csv.reader(src, delimiter=delimit)
		count = True
		for rows in my_reader :
			if count : 
				lst_markers = rows[1:]
				count = False
			else :
				A = objecttype(name=rows[0], sequence=rows[1:], markers=lst_markers)
				lst_of_objects.append(A)
		src.close()

	return lst_of_objects