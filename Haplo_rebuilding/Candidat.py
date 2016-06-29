#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from Haplotype import Haplotype
import itertools as it

class Candidat(Haplotype):
	def __init__(self, name, sequence, markers):
		"""Class constructor Candidat

		Haplotype legacy of class :
			-A name,
			-a sequence, 
			-a size who is the length of markers and
			-the list of there markers



		"""
		#Haplotype legacy of class
		Haplotype.__init__(self, name, sequence, markers)
		#Candidat specific to class
		self._geno_ori = ""
		self._haplo_ori = ""
		


	def __str__(self):
		"""Like str Haplotype a quick description of our Genotype object"""
		return "Candidait {}, constructed using {} markers, is : {}".format(self._name, self._nbmarkers, self._sequence)

	############
	#ACCESSEURS#
	############

	def _get_geno_ori(self):
		"""Return the attribut name of the Haplotype class"""
		return self._geno_ori

	def _get_haplo_ori(self):
		"""Return the attribut sequence of the Haplotype class"""
		return self._haplo_ori
	
	###########
	#MUTATEURS#
	###########

	def _set_geno_ori (self, newGenoOri):
		"""Change the name of our Haplotype object by a new one

		Named parameters :
		newname -- the new name selected (here first row of the input)
		
		"""
		self._geno_ori = newGenoOri

	def _set_haplo_ori(self, newHaploOri):
		"""Change the sequence list of our Haplotype object by a new one

		Named parameters :
		newsequence -- the new sequence list selected (here the end of the row in our input)
		
		"""
		self._haplo_ori = newHaploOri

	############
	#PROPERTIES#
	############

	geno_ori = property(_get_geno_ori, _set_geno_ori)
	haplo_ori = property(_get_haplo_ori, _set_haplo_ori)