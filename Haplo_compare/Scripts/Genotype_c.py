#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from Haplotype_c import Haplotype
import itertools as it

class Genotype(Haplotype):
	def __init__(self, name, sequence, markers):
		"""Class constructor Genotype

		Genotype Class is characterized by :
		Haplotype legacy of class :
			-A name,
			-a sequence, 
			-the list of there markers
		Genotype specific to class :
			-A number of Homozygous (Hmz) markers ('A', 'C', 'G' or 'T') (default = 0) maybe '--' for the new_haplotype,
			-a number of Heterozygous (Htz) markers (ex : '--' or 'A/G'), (default = 0)
			-a list of the Htz indexs in the Genotype object sequence,

		"""
		#Haplotype legacy of class
		Haplotype.__init__(self, name, sequence, markers)
		#Genotype specific to class
		self._nb_hmz_markers = 0
		self._nb_htz_markers = 0
		self._index_htz_markers = [] #Htz position site in genotype sequence (index list)
		self._index_bad_markers = [] #bad calling site in genotype sequence (index list)

	def __str__(self):
		"""Like str Haplotype a quick description of our Genotype object"""
		return "Haplotype {}, constructed using {} markers, is : {}".format(self._name, len(self._markers), self._sequence)


	############
	#ACCESSEURS#
	############

	def _get_nb_hmz_markers(self):
		"""Return the attribute that contains the number of Hmz markers"""
		return self._nb_hmz_markers

	def _get_nb_htz_markers(self):
		"""Return the attribute that contains the number of Htz markers"""
		return self._nb_htz_markers

	def _get_index_htz_markers(self):
		"""Return the attribute that contains a list with the indexs of Hmz markers"""
		return self._index_htz_markers_in_seq

	def _get_index_bad_markers(self):
		"""Return the attribute that contains a list with the indexs of '--' markers"""
		return self._index_bad_markers_in_seq
	
	###########
	#MUTATEURS#
	###########

	def _set_nb_hmz_markers(self, nb_hmz_markers):
		"""Changes the number of Hmz markers in genotype

		Named parameters :
		nb_hmz_markers -- a int (default = 0)

		"""
		self._nb_hmz_markers = nb_hmz_markers

	def _set_nb_htz_markers(self, nb_htz_markers):
		"""Changes the number of Htz markers in genotype

		Named parameters :
		nb_htz_markers -- a int (default = 0)

		"""
		self._nb_htz_markers = nb_htz_markers

	def _set_index_htz_markers(self, index_htz_markers):
		"""Changes the list of Htz markers indexs in genotype

		Named parameters :
		index_htz_markers -- a list (empty by default)

		"""
		self._index_htz_markers = index_htz_markers

	def _set_index_bad_markers(self, index_bad_markers):
		"""Changes the list of '--' markers indexs in genotype

		Named parameters :
		index_bad_markers -- a list (empty by default)

		"""
		self._index_bad_markers = index_bad_markers

	############
	#PROPERTIES#
	############

	nb_hmz_markers = property(_get_nb_hmz_markers, _set_nb_hmz_markers)
	nb_htz_markers = property(_get_nb_htz_markers, _set_nb_htz_markers)
	index_htz_markers = property(_get_index_htz_markers, _set_index_htz_markers)
	index_bad_markers = property(_get_index_bad_markers, _set_index_bad_markers)

	################
	#OTHER METHODES#
	################

	def htz_markers_position(self):
		"""Return a list of Htz positions sites of the relevant genotic sequence, 
		called 'htz_markers_position'.

		"""
		htz_pos = []
		# index list of htz SNP
		for nt in range(len(self.sequence)) :
			if len(self.sequence[nt]) == 3 :
				htz_pos.append(nt)
		return htz_pos

	def bad_markers_position(self):
		"""Return a list of bad calling ('--') positions sites of the relevant genotic sequence, 
		called 'htz_markers_position'.

		"""
		bad_pos = []
		# index list of '--' SNP
		for nt in range(len(self.sequence)) :
			if len(self.sequence[nt]) == 2 :
				bad_pos.append(nt)
		return bad_pos