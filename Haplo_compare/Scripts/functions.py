#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#Some functions

import csv

#Need have a special input file
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

	return lst_of_objects