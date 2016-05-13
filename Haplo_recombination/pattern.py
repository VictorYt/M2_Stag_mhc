#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#from Genotype import Genotype

class Pattern(object):
	def __init__(self, name, pattern_seq):
		"""Class constructor Haplotype

		Haplotype Class is characterized by :
			-A name, 
			-a sequence, 
			-a size who is the length of the sequence 
			-and haplotype origin.


		"""
		self._name = name 
		self._pattern_seq = pattern_seq 
		self._size = len(self.pattern_seq)
		self._haplo_ori = haplo_ori



	def __str__(self):
		"""Return a description of the created Haplotype object"""
		return "Pattern name : {}, length = {} have this sequence : {}".format(self._name, self._size, self._pattern_seq)

	############
	#ACCESSEURS#
	############

	def _get_name(self):
		"""Return the attribut name of the Pattern class"""
		return self._name

	def _get_pattern_seq(self):
		"""Return the attribut sequence of the Pattern class"""
		return self._pattern_seq

	def _get_size(self):
		"""Return the attribut size of the Pattern class """
		return self._size

	def _get_haplo_ori(self):
		"""Return True or Flase,
		False if the haplotype come from Homozygous Genotypes
		True if we find it previously by or Haplotype_rebuilding METHODES

		"""
		return self._haplo_ori

	###########
	#MUTATEURS#
	###########

	############
	#PROPERTIES#
	############

	################
	#OTHER METHODES#
	################