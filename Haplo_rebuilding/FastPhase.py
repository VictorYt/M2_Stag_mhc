#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from Haplotype import Haplotype
import itertools as it

class FastPhase(Haplotype):
	def __init__(self, name, sequence, markers):
		"""Class constructor FastPhase

		Haplotype legacy of class :
			-A name,
			-a sequence, 
			-a size who is the length of markers and
			-the list of there markers



		"""
		#Haplotype legacy of class
		Haplotype.__init__(self, name, sequence, markers)
		#FastPhase specific to class
		self._estimated_freq = ""
		self._estimated_square = ""
		


	def __str__(self):
		"""Like str Haplotype a quick description of our Genotype object"""
		return "Candidait {}, constructed using {} markers, is : {}".format(self._name, self._nbmarkers, self._sequence)

	############
	#ACCESSEURS#
	############

	def _get_estimated_freq(self):
		"""Return the estimated frequency of the FastPhase class"""
		return self._estimated_freq

	def _get_estimated_square(self):
		"""Return the attribut estimated square of the FastPhase class"""
		return self._estimated_square
	
	###########
	#MUTATEURS#
	###########

	def _set_estimated_freq (self, newFE):
		"""Change the estimated frequency of our FastPhase object by a new one

		Named parameters :
		newFE -- the new estimated frequency
		
		"""
		self._estimated_freq = newFE

	def _set_estimated_square(self, newSE):
		"""Change the estimated square list of our FastPhase object by a new one

		Named parameters :
		newSE -- the new estimated square	
		"""
		self._estimated_square = newSE

	############
	#PROPERTIES#
	############

	estimated_freq = property(_get_geno_ori, _set_geno_ori)
	estimated_square = property(_get_haplo_ori, _set_haplo_ori)