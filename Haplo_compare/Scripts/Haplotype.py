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
		self._half_geno_compatibility = []
		self._number_of_half_copatibility = 0
		self._entire_geno_compatibility = []
		self._number_of_entire_copatibility = 0



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

	def _get_half_geno_compatibility(self):
		"""Return a list of genotype instace with which our haplotype is compatible"""
		return self._half_geno_compatibility

	def _get_number_of_half_compatibility(self):
		"""Return the number of time our halpotype is compatible with the half genotype sequence.
		This number is the length of the list with the same name.

		"""
		return self._number_of_half_copatibility

	def _get_entire_geno_compatibility(self):
		"""Return a list of genotype instace with which our haplotype and a other confirme the entire sequence"""
		return self._entire_geno_compatibility

	def _get_number_of_entire_compatibility(self):
		"""Return the number of time our halpotype and another are compatible with the entire genotype sequence.
		This number is the length of the list with the same name.

		"""
		return self._number_of_entire_copatibility

#did i need to know with which one (haplotype) our haplotype is associated to have the entire genotype sequence?

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

	def _set_half_geno_compatibility(self, lsthalfcompatib):
		"""Change the compatibility list of half genotype instance with which our haplotype

		Named parameters :
		lsthalfcompatib -- the list of half geno compatibility

		"""
		self._half_geno_compatibility = lsthalfcompatib

	def _set_number_of_half_compatibility(self, number):
		"""Change the number of found genotype

		Named parameters :
		number -- the length of  our list of half geno compatibility

		"""		
		self._number_of_half_copatibility = number

	def _set_entire_geno_compatibility(self, lstentirecompatib):
		"""Change the compatibility list of entire genotype instance with which our haplotype

		Named parameters :
		lstentirecompatib -- the list of entire geno compatibility

		"""
		self._entire_geno_compatibility = lstentirecompatib

	def _set_number_of_entre_compatibility(self, number):
		"""Change the number of found genotype 

		Named parameters :
		number -- the length of  our list of entire geno compatibility

		"""
		self._number_of_entire_copatibility = number		

	############
	#PROPERTIES#
	############

	name = property(_get_name, _set_name)
	sequence = property(_get_sequence, _set_sequence)
	markers = property(_get_markers, _set_markers)
	half_geno_compatibility = property(_get_half_geno_compatibility, _set_half_geno_compatibility)
	number_of_half_copatibility = property(_get_number_of_half_compatibility, _set_number_of_half_compatibility)
	entire_geno_compatibility = property(_get_entire_geno_compatibility, _set_entire_geno_compatibility)
	number_of_entire_copatibility = property(_get_number_of_entire_compatibility, _set_entire_of_half_compatibility