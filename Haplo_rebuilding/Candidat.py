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
		self._index_htz_markers_in_seq = [] #liste des positions Htz dans seq du genotype (rend plus rapide la comparaison entre haplo possiblement combiné pour donner seq du génotype)
		


	def __str__(self):
		"""Like str Haplotype a quick description of our Genotype object"""
		return "Candidait {}, constructed using {} markers, is : {}".format(self._name, self._nbmarkers, self._sequence)
