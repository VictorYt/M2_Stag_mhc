#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Haplotype(object):
	def __init__(self, name, sequence, markers):
		"""Class constructor Haplotype

		Haplotype Class is characterized by :
			-A name, 
			-a sequence, 
			-a size who is the length of markers 
			-and the list of there markers

		During a second run with new haplotypes created, we add to the instance :
			-a list of the similar new haplotypes
			-the length of this list

		"""
		self._name = name 
		self._sequence = sequence 
		self._nbmarkers = len(self.sequence)
		self._markers = markers
		#generate during 2nd run
		self._similar_new_haplo = []
		self._number_of_similar_new_haplo = 0


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

	def _get_similar_new_haplo(self):
		"""Return the attribut similar_new_haplo of the Haplotype class which is
		a list the new haplotype who have the same sequence than our haplotype 
		
		"""
		return self._similar_new_haplo

	def _get_number_of_similar_new_haplo(self):
		"""Return the attribut number_of_similar_new_haplo of the Haplotype class which is 
		the size of the similar new haplotypes list
		
		"""
		return self._number_of_similar_new_haplo

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

	def _set_similar_new_haplo(self, newhaplo):
		"""Change the markers list of our Haplotype object by a new one

		Named parameters :
		newhaplo -- the similar new haplotype list of our genotype selected (here the Haplotype object ref)
		
		"""
		self._similar_new_haplo = newhaplo

	def _set_number_of_similar_new_haplo(self, newnbnewhaplo):
		"""Change the number of similar new haplotype size of our Haplotype object by a new one

		Named parameters :
		newnbnewhaplo -- the new size selected (here the length of similar_new_haplo list)
		
		"""
		self._number_of_similar_new_haplo = newnbnewhaplo

	############
	#PROPERTIES#
	############

	name = property(_get_name, _set_name)
	nbmarkers = property(_get_nbmarkers, _set_nbmarkers)
	sequence = property(_get_sequence, _set_sequence)
	markers = property(_get_markers, _set_markers)
	similar_new_haplo = property(_get_similar_new_haplo, _set_similar_new_haplo)
	number_of_similar_new_haplo = property(_get_number_of_similar_new_haplo, _set_number_of_similar_new_haplo)

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

	def screening_new_haplotype(self):
		"""Return a list of Haplotype objects who have the same new haplotye sequence 
		than the sequence of our Haplotype object.

		"""
		lst_similar_new_haplo = []
		for new_haplo in ... :
		return lst_similar_new_haplo