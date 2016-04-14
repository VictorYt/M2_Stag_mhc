#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#Haplotype daugther class


class Known_haplotype(Haplotype):
	"""docstring for Known_haplotype"""
	def __init__(self):
		super(Known_haplotype, self).__init__()
		self._half_geno_compatibility = []
		self._number_of_half_copatibility = 0
		self._entire_geno_compatibility = []
		self._number_of_entire_copatibility = 0