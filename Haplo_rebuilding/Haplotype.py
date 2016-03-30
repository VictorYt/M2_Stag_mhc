#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#from Genotype import Genotype


class Haplotype(object):
	def __init__(self, name, sequence, markers):
		"""Class constructor Haplotype

		Haplotype Class is characterized by :
			-A name, 
			-a sequence, 
			-a size who is the length of markers 
			-and the list of there markers

		During a second run with new haplotypes created, we add to the instance :
			-a list of the similar new haplotypes (same sequence after their been created)
			-the length of this list
			-a number of similar occurence (number of time an haplotype is find similar to a genotype)
			-the number of missing data by haplotype sequence

		"""
		self._name = name 
		self._sequence = sequence 
		self._nbmarkers = len(self.sequence)
		self._markers = markers
		#generate during 2nd run
		self._similar_new_haplotype = []
		self._number_of_similar_new_haplotype = 0
		self._similar_occurence = 0
		self._missing_data = 0


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

	def _get_similar_new_haplotype(self):
		"""Return the attribut similar_new_haplo of the Haplotype class which is
		a list the new haplotype who have the same sequence than our haplotype 
		
		"""
		return self._similar_new_haplotype

	def _get_number_of_similar_new_haplotype(self):
		"""Return the attribut number_of_similar_new_haplo of the Haplotype class which is 
		the size of the similar new haplotypes list
		
		"""
		return self._number_of_similar_new_haplotype

	def _get_similar_occurence(self):
		"""Return the number of time our haplotype is find similar to a genotype"""
		return self._similar_occurence

	def _get_missing_data(self):
		"""Return the number of missing data find in the genotype sequence"""
		return self._missing_data

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

	def _set_similar_new_haplotype(self, newhaplo):
		"""Change the markers list of our Haplotype object by a new one

		Named parameters :
		newhaplo -- the similar new haplotype list of our genotype selected (here the Haplotype object ref)
		
		"""
		self._similar_new_haplotype = newhaplo

	def _set_number_of_similar_new_haplotype(self, newnbnewhaplo):
		"""Change the number of similar new haplotype size of our Haplotype object by a new one

		Named parameters :
		newnbnewhaplo -- the new size selected (here the length of similar_new_haplo list)
		
		"""
		self._number_of_similar_new_haplotype = newnbnewhaplo

	def _set_similar_occurence(self, nboccurence):
		"""Change the number of time the haplotype is find similar with a genotype

		Named parameters :
		nboccurence -- the new time haplotype be similar with genotype

		"""
		self._similar_occurence = nboccurence

	def _set_missing_data(self, nbmssingdata):
		"""Change the number of missing data find in the genotype sequence

		Named parameters :
		nbmssingdata -- the new number of missing data find in the genotype sequence

		"""
		self._missing_data = nbmssingdata

	############
	#PROPERTIES#
	############

	name = property(_get_name, _set_name)
	nbmarkers = property(_get_nbmarkers, _set_nbmarkers)
	sequence = property(_get_sequence, _set_sequence)
	markers = property(_get_markers, _set_markers)
	similar_new_haplotype = property(_get_similar_new_haplotype, _set_similar_new_haplotype)
	number_of_similar_new_haplotype = property(_get_number_of_similar_new_haplotype, _set_number_of_similar_new_haplotype)
	similar_occurence = property(_get_similar_occurence, _set_similar_occurence)
	missing_data = property(_get_missing_data, _set_missing_data)

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

	#chaud mais serait bien à faire fonctionner
	def screening_himself(self, lst_of_new_haplotype):
		"""Return a list of Haplotype objects who have the same new haplotye sequence 
		than the sequence of our Haplotype object.

		"""
		#étape pour se trouver lui même dans la liste et s'éviter après
		index_me = 0
		for me in lst_of_new_haplotype:
			if me.name == self.name :
				index_me = lst_of_new_haplotype.index(me)

		lst_similar_new_haplo = []
		for same in lst_of_new_haplotype :
			if lst_of_new_haplotype.index(same) == index_me :
				pass
			elif same.sequence == self.sequence :
				lst_similar_new_haplo.append(same)
		return lst_similar_new_haplo

	def occurence_new_haplotype(self, lst_of_genotype):
		"""Return the number of time the haplotype is similar with a different genotype

		By defaut a new_haplotype must appear at least one time, if he appear more than that 
		we can concider him like a good one to add in our haplotype catalog

		"""
		occurence = 0
		for geno in lst_of_genotype :
			if self in geno.similar_haplotype :
				occurence +=1
		return occurence

	def missing_data_counter(self):
		"""Return nothing but grow the number of missing data of each Haplotype each time it appear 
		in the haplotype sequence
		By default missing_data = 0

		"""
		for values in self.sequence :
			if values == "--" :
				self.missing_data += 1