#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Haplotype(object):
	def __init__(self, name, sequence, markers):
		"""Class constructor Haplotype

		Haplotype Class is characterized by :
		A name, a sequence, a size who is the length of markers and
		the list of there markers

		"""
		self._name = name 
		self._sequence = sequence 
		self._nbmarkers = len(self.sequence)
		self._markers = markers 


	def __str__(self):
		"""Return a description of the created Haplotype object"""
		return "L'haplotype {}, construit à l'aide de {} marqueurs, est : {}".format(self._name, self._nbmarkers, self._sequence)

	############
	#ACCESSEURS#
	############

	def _get_name(self):
		"""Return the attribut name of the Haplotype class"""
		return self._name

	def _get_sequence(self):
		"""Return the attribut sequence of the Haplotype class"""
		return self._sequence

	def _get_nbmarkers(self):
		"""Return the attribut nbmarkers of the Haplotype class which is 
		the sequence size
		
		"""
		return self._nbmarkers

	def _get_markers(self):
		"""Return the attribut markers of the Haplotype class which is
		a list of the markers name used for genotyping 
		
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

	def _set_nbmarkers(self, newnbmarkers):
		"""Change the sequence size of our Haplotype object by a new one

		Named parameters :
		newnbmarkers -- the new sequence size selected (here the length of markers)
		
		"""
		self._nbmarkers = newnbmarkers

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
	nbmarkers = property(_get_nbmarkers, _set_nbmarkers)
	sequence = property(_get_sequence, _set_sequence)
	markers = property(_get_markers, _set_markers)

	################
	#OTHER METHODES#
	################

	#polymorphisme (surcharge) avec la fonction compare_geno_and_haplo_seq(self, geno, haplo) ==> voir comment ça marche
	def compare_two_seq(self, haplo1, haplo2):
		"""Return a list with the name of the 2 Haplotypes objects,
		a sequence with booleen (0, 1) and a int

		0 means no differences between the 2 haplotypes sequence for the selected markers 
		1 means that there is a difference
		The int in the end of the returned list is the sum of 1 in the sequence.

		Named parameters :
		haplo1 -- The fisrt Haplotype object to compare
		haplo2 -- The second Haplotype object to compare

		"""
		ligne_de_sortie = []
		count_erreur = 0
		ligne_de_sortie.append(haplo1.name)
		ligne_de_sortie.append(haplo2.name)
		for i in range(len(haplo1.sequence)) :
			#Equal to 1 in the case of fail or impossible calling for some markers
			if len(haplo1.sequence[i]) == 1 :
				if haplo1.sequence[i] == haplo2.sequence[i] :
					ligne_de_sortie.append(0)
				else :
					ligne_de_sortie.append(1)
					count_erreur += 1
			#If we have one of them ('--') we concidere there are no differrence 
			else :
				ligne_de_sortie.append(0)
		ligne_de_sortie.append(count_erreur)
		return ligne_de_sortie