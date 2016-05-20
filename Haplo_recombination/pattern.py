#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#from Genotype import Genotype

class Pattern(object):
	def __init__(self, pattern_name, pattern_seq):
		"""Class constructor Haplotype

		Haplotype Class is characterized by :
			-A name, 
			-a sequence, 
			-a size who is the length of the sequence 
			-a haplotype origin.
			-and a haplotype who it look like


		"""
		self._pattern_name = pattern_name 
		self._pattern_seq = pattern_seq 
		self._size = len(self.pattern_seq)
		self._haplo_ori = haplo_ori
		self._



	def __str__(self):
		"""Return a description of the created Haplotype object"""
		return "Pattern name : {}, length = {} have this sequence : {}".format(self._pattern_name, self._size, self._pattern_seq)

	############
	#ACCESSEURS#
	############

	def _get_pattern_name(self):
		"""Return the attribut name of the Pattern class"""
		return self._pattern_name

	def _get_pattern_seq(self):
		"""Return the attribut sequence of the Pattern class"""
		return self._pattern_seq

	def _get_size(self):
		"""Return the attribut size of the Pattern class """
		return self._size

	def _get_haplo_ori(self):
		"""Return the Haplotype attribut where the Pattern attribut comme from"""
		return self._haplo_ori

	###########
	#MUTATEURS#
	###########

	def _set_pattern_name(self, name):
		"""Return the attribut name of the Pattern class"""
		self._pattern_name = name

	def _set_pattern_seq(self,sequence):
		"""Return the attribut sequence of the Pattern class"""
		self._pattern_seq = sequence

	def _set_size(self, length):
		"""Return the attribut size of the Pattern class """
		self._size = length

	def _set_haplo_ori(self, H_ori):
		"""Return the Haplotype attribut where the Pattern attribut comme from"""
		self._haplo_ori = H_ori

	############
	#PROPERTIES#
	############

	pattern_name = property(_get_pattern_name, _set_pattern_name)
	pattern_seq = property(_get_pattern_seq, _set_pattern_seq)
	size = property(_get_size, _set_size)
	haplo_ori = property(_get_haplo_ori, _set_haplo_ori)

	################
	#OTHER METHODES#
	################