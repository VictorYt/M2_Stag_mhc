#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import itertools as it


class Haplotype(object):
	def __init__(self, name, sequence, markers):
		"""Class constructor Haplotype

		Haplotype Class is characterized by :
			-A name, 
			-a sequence, 
			-a size who is the length of markers 
			-and the list of there markers
			-a origin (how i obtain it [default: Known])

		During the first run with our knowned Haplotypes and our Genotypes
			-a list of genotype instance for which our haplotype instance have a maximum of threshold missmatch with genotype
			-a list of genotype which are obtain with the combination of this haplotype and another known one.

		During a second run with new haplotypes created, we add to the instance :
			-a list of the similar new haplotypes (same sequence after their been created)
			-the length of this list
			-a number of similar occurence (number of time a Candidate Haplotype is créé by different Haplotypes and Genotypes)
			-the number of missing data by haplotype sequence

		"""
		self._name = name 
		self._sequence = sequence 
		self._nbmarkers = len(self.sequence)
		self._markers = markers
		self._origin = "Known"
		#generate during 1st run
		self._half_similarity_with = {}
		self._half_similarity_number = {} #not use can be deleted i use len(...)
		self._good_combination = [] #not use now
		#generate during 2nd run
		self._similar_new_haplotype = [] 
		self._number_of_similar_new_haplotype = 0 
		self._similar_occurence = 0
		self._missing_data = 0


	def __str__(self):
		"""Return a description of the created Haplotype object"""
		return "Haplotype {}, constructed using {} markers, is a {} : {}".format(self._name, self._nbmarkers, self.origin, self._sequence)

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
		a list of the markers names used for genotyping 
		
		"""
		return self._markers

	def _get_origin(self):
		"""Return the attribut origin of the Haplotype class which is
		a string who is Known by default but can also be "candidate" or "fastPHASE".

		"""
		return self._origin

	def _get_half_similarity_with(self):
		"""Return the attribut half_similarity_with of the Haplotype class which is 
		a dictionary with keys to the range [0; threshold]. The keys have the values, 
		a list of genotype, for which our haplotype have n missmatch.
		n = keys values

		"""
		return self._half_similarity_with

	def _get_half_similarity_number(self):
		"""Return the attribut half_similarity_number of the Haplotype class which is
		a dictionary with keys to the range [0; threshold]. The keys have the values, 
		the length of the list the attriut half_similarity_with which the same keys."""
		return self._half_similarity_number

	def _get_good_combination(self):
		"""Return the attribut good_combination of the Haplotypes class which is
		a list of Genotypes, which his obtain with our haplotypes and another one (which also have a half_similarity_with the same genotype, and 0 missmatch).

		"""
		return self._good_combination

	def _get_similar_new_haplotype(self):
		"""Return the attribut similar_new_haplo of the Haplotype class which is
		a list of candidate haplotype who have the similar sequence than our haplotype 
		
		"""
		return self._similar_new_haplotype

	def _get_number_of_similar_new_haplotype(self):
		"""Return the attribut number_of_similar_new_haplo of the Haplotype class which is 
		the size of the similar new haplotypes list
		
		"""
		return self._number_of_similar_new_haplotype

	def _get_similar_occurence(self):
		"""Return the number of time our candidate haplotype is find similar to a genotype"""
		return self._similar_occurence

	def _get_missing_data(self):
		"""Return the number of missing data find in the candidate haplotype sequence"""
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

	def _set_origin(self, neworigin):
		"""Change the origin string of our Haplotype object by a new one

		Named parameters :
		neworigin -- the new origin string selected (here "candidate" or "fastPHASE")
		
		"""
		self._origin = neworigin

	def _set_half_similarity_with(self, dicoofsimilarity):
		"""Change the half_similarity_with dictionary of our Haplotype object by a new one

		Named parameters :
		dicoofsimilarity -- the new half_similarity dictionary selected (his size depend of threshold choise in the comande)
		
		"""
		self._half_similarity_with = dicoofsimilarity

	def _set_half_similarity_number(self, dicosimnumb):
		"""Change the half_similarity_number dictionary of our Haplotype object by a new one

		Named parameters :
		dicosimnumb -- the new half_similarity dictionary selected with length of list in my dico (his size depend of threshold choise in the comande)
		
		"""
		self._half_similarity_number = dicosimnumb

	def _set_good_combination(self, listofgoodcombi):
		"""Change the good_combination list of our Haplotype object by a new one

		Named parameters :
		dicoofsimilarity -- the new good_combination list selected (this is the genotype obtain by a combination of 2 Known Haplotypes)
		
		"""
		self._good_combination = listofgoodcombi

	def _set_similar_new_haplotype(self, newhaplo):
		"""Change the candidate haplotype list of our Haplotype object by a new one

		Named parameters :
		newhaplo -- the similar candidate haplotype list of our genotype selected (here the Haplotype object ref)
		
		"""
		self._similar_new_haplotype = newhaplo

	def _set_number_of_similar_new_haplotype(self, nbnewhaplo):
		"""Change the similar candidate haplotype size of our Haplotype object by a new one

		Named parameters :
		newnbnewhaplo -- the new size selected (here the length of similar_new_haplo list)
		
		"""
		self._number_of_similar_new_haplotype = nbnewhaplo

	def _set_similar_occurence(self, nboccurence):
		"""Change the number of time the haplotype is find similar with a genotype

		Named parameters :
		nboccurence -- the new time haplotype be similar with genotype

		"""
		self._similar_occurence = nboccurence

	def _set_missing_data(self, nbmssingdata):
		"""Change the number of missing data find in the haplotype sequence

		Named parameters :
		nbmssingdata -- the new number of missing data find in the haplotype sequence

		"""
		self._missing_data = nbmssingdata

	############
	#PROPERTIES#
	############

	name = property(_get_name, _set_name)
	nbmarkers = property(_get_nbmarkers, _set_nbmarkers)
	sequence = property(_get_sequence, _set_sequence)
	markers = property(_get_markers, _set_markers)
	origin = property(_get_origin, _set_origin)
	half_similarity_with = property(_get_half_similarity_with, _set_half_similarity_with)
	half_similarity_number = property(_get_half_similarity_number, _set_half_similarity_number)
	good_combination = property(_get_good_combination, _set_good_combination)
	similar_occurence = property(_get_similar_occurence, _set_similar_occurence)	
	similar_new_haplotype = property(_get_similar_new_haplotype, _set_similar_new_haplotype)
	number_of_similar_new_haplotype = property(_get_number_of_similar_new_haplotype, _set_number_of_similar_new_haplotype)
	missing_data = property(_get_missing_data, _set_missing_data)

	################
	#OTHER METHODES#
	################

	#verify if the other work for haplo, geno. if it's work delete this want
	def compare_two_seq2(self, haplo):
		"""Return a list with the name of the 2 Haplotypes objects,
		a sequence with booleen (0, 1) and a int

		0 means no missmatch between the 2 Haplotypes sequence objects for the selected markers 
		1 means that there is a missmatch
		The int at the end of the returned list is the sum of 1 in the sequence 
		(= number of missmatch).

		Named parameters :
		haplo -- The Haplotype object to compare with mine

		"""
		output_line = []
		count_erreur = 0
		#add ib the output_line list the name of the 2 sequences compared
		output_line.append(self.name)
		output_line.append(haplo.name)
		for i in range(len(self.sequence)) :
			#traitment of Hmz Markers
			if len(self.sequence[i]) == 1 :
				if self.sequence[i] == haplo.sequence[i] :
					output_line.append(0)
				else :
					output_line.append(1)
					count_erreur += 1
			#traitment of unknowing base for markers ('--')
			elif len(self.sequence[i]) == 2 :
				output_line.append(0)
			#traitment of Htz markers
			elif len(self.sequence[i]) == 3 :
				if self.sequence[i].rsplit("/", 1)[0] != haplo.sequence[i] :
					if self.sequence[i].rsplit("/", 1)[1] != haplo.sequence[i] :
						output_line.append(1)
						count_erreur += 1
					else :
						output_line.append(0)
				else :
					output_line.append(0)
		output_line.append(count_erreur)
		#print (len(output_line)) #--> need be equal to (len(markers) + geno.name(=1) + haplo.name(=1) + sum(count_erreur)(=1) so len(markers)+3)
		return output_line

	#new method, work with all threshold
	def compare_two_seq(self, objects):
		"""Return a list with the name of the 2 objects,
		a sequence with booleen (0, 1) and a int.

		0 means no missmatch between the 2 sequences objects for the selected markers 
		1 means that there is a missmatch
		The int at the end of the returned list is the sum of 1 in the sequence 
		(= number of missmatch).

		Named parameters :
		objects -- The object to compare with mine

		"""
		output_line = []
		count_erreur = 0
		#add ib the output_line list the name of the 2 sequences compared
		output_line.append(self.name)
		output_line.append(objects.name)
		#marche pour comparer 1 geno a un haplo
		#I look what kind of objets i have
		#if it's a Haplotype object i look the self.sequence (because it can be my Genotype object, if it's an Haplotype, no prob because my object is a Haplotype Ast condition works)
		if type(objects) is Haplotype :
			for i in range(len(self.sequence)) :
				#traitment of Hmz Markers
				if len(self.sequence[i]) == 1 : #1st condition
					if self.sequence[i] == objects.sequence[i] :
						output_line.append(0)
					else :
						output_line.append(1)
						count_erreur += 1
				#traitment of unknowing base for markers ('--')
				elif len(self.sequence[i]) == 2 : #2nd condition
					output_line.append(0)
				#traitment of Htz markers
				elif len(self.sequence[i]) == 3 : #3rd condition
					if self.sequence[i].rsplit("/", 1)[0] != objects.sequence[i] :
						if self.sequence[i].rsplit("/", 1)[1] != objects.sequence[i] :
							output_line.append(1)
							count_erreur += 1
						else :
							output_line.append(0)
					else :
						output_line.append(0)
			output_line.append(count_erreur)
		#if my objets is a Genotype, i look the object.sequence (because in known that i have a Genotype object here)
		else :
			for i in range(len(self.sequence)) :
				#traitment of Hmz Markers
				if len(objects.sequence[i]) == 1 :
					if self.sequence[i] == objects.sequence[i] :
						output_line.append(0)
					else :
						output_line.append(1)
						count_erreur += 1
				#traitment of unknowing base for markers ('--')
				elif len(objects.sequence[i]) == 2 :
					output_line.append(0)
				#traitment of Htz markers
				elif len(objects.sequence[i]) == 3 :
					if objects.sequence[i].rsplit("/", 1)[0] != self.sequence[i] :
						if objects.sequence[i].rsplit("/", 1)[1] != self.sequence[i] :
							output_line.append(1)
							count_erreur += 1
						else :
							output_line.append(0)
					else :
						output_line.append(0)
			output_line.append(count_erreur)
		#print (len(output_line)) #--> need be equal to (len(markers) + geno.name(=1) + objects.name(=1) + sum(count_erreur)(=1) so len(markers)+3)
		return output_line

	def similar_with_size(self, threshold):
		"""Return a empty dictionary with keys equal at [0,threshold]
		This dictionnary will be fill (for each keys) by the genotype istance who have half of is sequence
		similar to our haplotype.

		"""
		dico = {}
		for i in range(int(threshold)+1) :
			dico[i] = []
		return dico#change this functoin name


	def select_similar_with(self, objects, threshold):
		"""Return nothing but fill the dictionnary created before"""
		#with the previusly created dictionnary :
		try :
			sum_mismatch = self.compare_two_seq(objects)[-1]
			if int(sum_mismatch) <= int(threshold) :
				self.half_similarity_with[sum_mismatch].append(objects)
		except KeyError :
			print ("You have a problem in 'select_similar_with' method, check it")
			print (self.compare_two_seq(objects))
			print (self.half_similarity_with)
			raise#ch



	#maybe a way to do this quickly
	def screening_himself(self, lst_of_candidate_haplotype):
		"""Return a list of Haplotype objects who have the same new haplotye sequence 
		than the sequence of our Haplotype object.

		"""
		#Find himself in the list
		index_me = 0
		for me in lst_of_candidate_haplotype:
			if me.name == self.name :
				index_me = lst_of_candidate_haplotype.index(me)

		lst_similar_new_haplo = []
		for same in lst_of_candidate_haplotype :
			#if he find himslef i pass
			if lst_of_candidate_haplotype.index(same) == index_me :
				pass
			#for all the other i compare the sequence
			elif same.sequence == self.sequence :
				lst_similar_new_haplo.append(same)
				#if 2 Haplotype instance have the same sequence i have the second in the list of similar instance of that i'm looking for
		return lst_similar_new_haplo

	#maybe a way to do this quickly
	def screening_himself_test(self, lst_of_candidate_haplotype):
		"""Return a list of Haplotype objects who have the same new haplotye sequence 
		than the sequence of our Haplotype object.

		"""
		#Find himself in the list
		index_me = 0
		for me in lst_of_candidate_haplotype:
			if me == self :
				index_me = lst_of_candidate_haplotype.index(me)

		lst_similar_new_haplo = []
		for same in lst_of_candidate_haplotype :
			#if he find himslef i pass
			if lst_of_candidate_haplotype.index(same) == index_me :
				pass
			#for all the other i compare the sequence
			elif same.sequence == self.sequence :
				lst_similar_new_haplo.append(same)
				#if 2 Haplotype instance have the same sequence i have the second in the list of similar instance of that i'm looking for
		return lst_similar_new_haplo

	def similarity_time_with(self):
		"""Return a int who is the number of time this Haplotype is find Half_similar with a Genotype"""
		number_of_time = 0
		for i in self.half_similarity_with.keys() :
			number_of_time += len(self.half_similarity_with[i])
		return number_of_time

	def occurence_candidaite_haplotype(self, lst_of_genotype):
		"""Return the number of time the haplotype is similar with a different genotype

		By defaut a new_haplotype must appear at least one time, if he appear more than that 
		we can concider him like a good candidate to add in our haplotype catalog

		"""
		occurence = 0
		for geno in lst_of_genotype :
			if self in geno.similar_haplotype :
				occurence +=1
		return occurence

	#do a similar funtion to know what candidates haplotypes are correct during there creation
	def missing_data_counter(self):
		"""Return nothing but grow the number of missing data of each Haplotype each time it appear 
		in the haplotype sequence
		By default missing_data = 0

		"""
		for values in self.sequence :
			if values == "--" :
				self.missing_data += 1