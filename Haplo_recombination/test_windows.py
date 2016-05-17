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
		header = True
		for rows in my_reader :
			if header : 
				lst_markers = rows[1:]
				header = False
			else :
				A = objecttype(name=rows[0], sequence=rows[1:], markers=lst_markers)
				lst_of_objects.append(A)
		src.close()

	return lst_of_objects




def KnuthMorrisPratt(text, pattern):
	"""Yields all starting positions of copies of the pattern in th text. 
	Calling conventions are similar to string.find, but it's arguments can be lists
	or iterators, not just strings, it returns all matches, no just the first one,
	and it does not need the whole text in memory at once. 
	Whenever it yields, it will have read the text exactly up to and
	including the match that cused the yeild. 

	"""
	#allow indiexing into pattern and protect against change during yield
	pattern = list(pattern) #attention je lui donnerai dejà une liste

	#build table of shift amounts
	shifts = [1] * (len(pattern) +1)
	shift = 1
	for pos in range(len(pattern)):
		while shift <= pos and pattern[pos] != pattern[pos-shift]:
			shift += shifts[pos-shift]
		shifts[pos+1] = shift

	#do the actual search
	startPos = 0
	matchLen = 0
	for c in text :
		while matchLen == len(pattern) or matchLen >= 0 and pattern[matchLen] != c :
			startPos += shifts[matchLen]
			matchLen -= shifts[matchLen]
		matchLen += 1
		if matchLen == len(pattern) :
			yield startPos