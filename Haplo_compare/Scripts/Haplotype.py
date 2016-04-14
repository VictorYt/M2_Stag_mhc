#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#Haplotype mother class

class Haplotype(object):
		def __init__(self, name, sequence, markers):
			"""Class constructor Haplotype

			Haplotype Class is characterized by :
				-A name, 
				-a sequence

			"""
			self._name = name 
			self._sequence = sequence
			self._markers = markers

		############
		#ACCESSEURS#
		############

		def _get_name(self):
			"""Return the attribut name of the Haplotype class"""
			return self._name

		def _get_sequence(self):
			"""Return the attribut sequence of the Haplotype class"""
			return self._sequence

		def _get_markers(self):
			"""Return the attribut markers of the Haplotype class which is
			a list of the markers names used for genotyping 
			
			"""
			return self._markers

		###########
		#MUTATEURS#
		###########

		def _set_name (self, newname):
			"""Change the name of our Haplotype object by a new one

			Named parameters :
			newname -- the new name selected (here first row of the input)
			
			"""
			self._name = newname

		def _set_sequence(self, newsequence):
			"""Change the sequence list of our Haplotype object by a new one

			Named parameters :
			newsequence -- the new sequence list selected (here the end of the row in our input)
			
			"""
			self._sequence = sequence

		def _set_markers(self, lstmarkers):
			"""Change the markers list of our Haplotype object by a new one

			Named parameters :
			lstmarkers -- the new markers list selected (here the header of the input)
			
			"""
			self._markers = lstmarkers 

		############
		#PROPERTIES#
		############

		name = property(_get_name, _set_name)
		sequence = property(_get_sequence, _set_sequence)
		markers = property(_get_markers, _set_markers)