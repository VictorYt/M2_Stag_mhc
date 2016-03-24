#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from Haplotype import Haplotype
import itertools as it

class Genotype(Haplotype):
	def __init__(self, name, sequence, markers):
		"""Class constructor Genotype

		Genotype Class is characterized by :
		Haplotype legacy of class :
			-A name,
			-a sequence, 
			-a size who is the length of markers and
			-the list of there markers
		Genotype specific to class :
			#generate during the 1st run
			-A number of Homozygous (Hmz) markers ('A', 'C', 'G' or 'T') (default = 0) maybe '--' for the new_haplotype,
			-a number of Heterozygous (Htz) markers (ex : '--' or 'A/G'), (default = 0)
			-a list of the Htz indexs in the Genotype object sequence,
			-a list of Haplotype(s) object(s) who are similar to our genotype
			(sum of errors in each markers positions = ... 0 1 ou 2) 
			-the size of this list (default = 0).
			-a list of probable combination of similar haplotypes that allows us to
			obtain the genotype.
			-the size of this list (default = 0).
			-a new haplotype list filled if there is at least 1 similar haplotype and
			no prbable combination.
			-the size of this list (default = 0).
			
			#generate during the 2nd run
			-a new list of probable combination of similar haplotypes that allows us to
			obtain the genotype.Because, we add in similar haplotype list the new haplotype
			created during the first run which are similar to our genotype
			-the size of this list (default = 0).

			something more?

		"""
		#Haplotype legacy of class
		Haplotype.__init__(self, name, sequence, markers)
		#Genotype specific to class
		self._nb_hmz_markers = 0
		self._nb_htz_markers = 0
		self._index_htz_markers_in_seq = [] #liste des positions Htz dans seq du genotype (rend plus rapide la comparaison entre haplo possiblement combiné pour donner seq du génotype)
		self._similar_haplotype = [] #une liste de sequences (eux même des liste de caractères)
		self._number_of_similar_haplotype = 0 #taille de la liste obtenue ci-dessus
		self._probable_haplotypes_combinaison = [] #liste de liste (ex: [[haplo1, haplo4], [haplo20, haplo79]])
		self._number_of_probable_haplotypes_combinaison = 0	
		self._lst_of_new_haplotype = [] #une liste de nouveau(x) (pour le moment liste de la séqeunce seul) haplotype(s) créé à partir de l'objet Génotype en question
		self._number_of_new_created_haplotype = 0 #taille de la liste obtenue ci-dessus
		self._probable_haplotypes_combinaison_2_run = [] # nouvelle liste de combinaison 
		self._number_of_probable_haplotypes_combinaison_2_run = 0

	def __str__(self):
		"""Like str Haplotype a quick description of our Genotype object"""
		return "Le Genotype {}, construit à l'aide de {} marqueurs, est : {}".format(self._name, self._nbmarkers, self._sequence)


	############
	#ACCESSEURS#
	############

	def _get_nb_hmz_markers(self):
		"""Return the attribute that contains the number of Hmz markers"""
		return self._nb_hmz_markers

	def _get_nb_htz_markers(self):
		"""Return the attribute that contains the number of Htz markers"""
		return self._nb_htz_markers

	def _get_index_htz_markers_in_seq(self):
		"""Return the attribute that contains a list with the indexs of Hmz markers"""
		return self._index_htz_markers_in_seq
	
	def _get_similar_haplotype(self):
		"""Return the attribute that contains a Haplotype object list  
		similar to our genotype

		"""
		return self._similar_haplotype

	def _get_number_of_similar_haplotype(self):
		"""Return the attribute that contains the size of the similar Haplotype object list"""
		return self._number_of_similar_haplotype

	def _get_probable_haplotypes_combinaison(self):
		"""Return the attribut that contains the list of combination of similar Haplotype object  
		that allows us to obtain the genotype.

		"""
		return self._probable_haplotypes_combinaison

	def _get_number_of_probable_haplotypes_combinaison(self):
		"""Return the attribute that contains the size of the previous list above"""
		return self._number_of_probable_haplotypes_combinaison		

	def _get_lst_of_new_haplotype(self):
		"""Return the attribut that contains the list of new haplotypes obtained."""
		return self._lst_of_new_haplotype

	def _get_number_of_new_created_haplotype(self):
		"""Return the attribute that contains the size of the previous list above"""
		return self._number_of_new_created_haplotype

	def _get_probable_haplotypes_combinaison_2_run(self):
		"""Return the attribut that contains the list of combination of similar Haplotype object 
		(enlarged by new haplotype created in the 1st run)
		that allows us to obtain the genotype.

		"""
		return self._probable_haplotypes_combinaison_2_run

	def _get_number_of_probable_haplotypes_combinaison_2_run(self):
		"""Return the attribute that contains the size of the previous list above"""
		return self._number_of_probable_haplotypes_combinaison_2_run	

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

	def _set_index_htz_markers_in_seq(self, index_htz_markers):
		"""Changes the list of Htz markers indexs in genotype

		Named parameters :
		index_htz_markers -- a list (empty by default)

		"""
		self._index_htz_markers_in_seq = index_htz_markers
	
	def _set_similar_haplotype(self, similar_haplotype):
		"""Changes the list of similar haplotype with our genotype

		Named parameters :
		similar_haplotype -- a list (empty by default)

		"""
		self._similar_haplotype = similar_haplotype

	def _set_number_of_similar_haplotype(self, nb_similar_haplotype):
		"""Changes the number of similar haplotype with our genotype

		Named parameters :
		nb_similar_haplotype -- a int (default = 0)

		"""
		self._number_of_similar_haplotype = nb_similar_haplotype

	def _set_probable_haplotypes_combinaison(self, haplo_combinaison):
		"""Changes the list of probable combination of haplotype which can give our genotype 

		Named parameters :
		haplo_combinaison -- a list (empty by default)

		"""
		self._probable_haplotypes_combinaison = haplo_combinaison

	def _set_number_of_probable_haplotypes_combinaison(self, nb_haplo_combinaison):
		"""Changes the number of probable combination we find above

		Named parameters :
		nb_haplo_combinaison -- a int (default = 0)

		"""
		self._number_of_probable_haplotypes_combinaison = nb_haplo_combinaison

	def _set_lst_of_new_haplotype(self, new_haplotype):
		"""Changes the list of new haplotype which can give our genotype 
		when knowing a similar haplotype without probable combination.
		Please note that this list doesn't contain Haplotype objects (like previous)
		but lists for the newly created sequences.
 

		Named parameters :
		new_haplotype -- a list (empty by default)

		"""
		self._lst_of_new_haplotype = new_haplotype

	def _set_number_of_new_created_haplotype(self, new_number):
		"""Changes the number to the size of new haplotype list

		Named parameters :
		new_number -- a int (default = 0)

		"""
		self._number_of_new_created_haplotype = new_number

	def _set_probable_haplotypes_combinaison_2_run(self, new_similar_haplotype):
		"""Changes the list of probable combination (2nd run) of haplotype which can give our genotype 

		Named parameters :
		haplo_combinaison -- a list (default = probable_haplotypes_combinaison)

		"""
		self._probable_haplotypes_combinaison_2_run = new_similar_haplotype

	def _set_number_of_probable_haplotypes_combinaison_2_run(self, new_nb_haplo_combinaison):
		"""Changes the number of probable combination we find above

		Named parameters :
		new_nb_haplo_combinaison -- a int (default = nb_haplo_combinaison)

		"""
		self._number_of_probable_haplotypes_combinaison_2_run = new_nb_haplo_combinaison

	############
	#PROPERTIES#
	############

	nb_hmz_markers = property(_get_nb_hmz_markers, _set_nb_hmz_markers)
	nb_htz_markers = property(_get_nb_htz_markers, _set_nb_htz_markers)
	index_htz_markers_in_seq = property(_get_index_htz_markers_in_seq, _set_index_htz_markers_in_seq)
	similar_haplotype = property(_get_similar_haplotype, _set_similar_haplotype)
	number_of_similar_haplotype = property(_get_number_of_similar_haplotype, _set_number_of_similar_haplotype)
	probable_haplotypes_combinaison = property(_get_probable_haplotypes_combinaison, _set_probable_haplotypes_combinaison)
	number_of_probable_haplotypes_combinaison = property(_get_number_of_probable_haplotypes_combinaison, _set_number_of_probable_haplotypes_combinaison)
	lst_of_new_haplotype = property(_get_lst_of_new_haplotype, _set_lst_of_new_haplotype)
	number_of_new_created_haplotype = property(_get_number_of_new_created_haplotype, _set_number_of_new_created_haplotype)
	probable_haplotypes_combinaison_2_run = property(_get_probable_haplotypes_combinaison_2_run, _set_probable_haplotypes_combinaison_2_run)
	number_of_probable_haplotypes_combinaison_2_run = property(_get_number_of_probable_haplotypes_combinaison_2_run, _set_number_of_probable_haplotypes_combinaison_2_run)

	################
	#OTHER METHODES#
	################

	#attention je prend en compte les erreur de calling (--) dans le compte des Htz
	#erreur d'indexation ===> a corriger
	def position_htz_markers(self):
		"""Returns list of Htz positions sites (or bad calling) of the relevant genotic sequence, 
		called 'position_htz_markers'.

		"""
		position_htz_markers = []
		for nt in range(len(self.sequence)) : 
			if len(self.sequence[nt]) > 1 :
				position_htz_markers.append(nt)
			else :
				pass
		return position_htz_markers

	def have_nb_htz_markers(self):
		"""Return the number of Htz markers by checking the length of the list
		recovering by the function position_htz_markers()

		"""
		return len(self._index_htz_markers_in_seq)

	def have_nb_hmz_markers(self):
		"""Return the number of Hmz markers by subtracting the total number of markers (_nbmarkers)
		with the number of Htz markers (find with have_nb_htz_markers())

		"""
		return self._nbmarkers - self._nb_htz_markers 

	#An overload method
	def compare_two_seq(self, geno, haplo):
		"""Overload of the same name method in the Haplotype object
		Return a list with the name of the Genotype objets and the Haplotypes objects,
		a sequence with booleen (0, 1) and a int.
		The difference with the other is the use of a genomic sequence who contain htz markers
		and fail calling markers ('--').

		0 means no differences between the 2 haplotypes sequence for the selected markers 
		1 means that there is a difference
		The int in the end of the returned list is the sum of 1 in the sequence.

		Named parameters :
		geno -- The Genotype object to compare
		haplo -- The Haplotype object to compare

		"""
		ligne_de_sortie = []
		count_erreur = 0
		#add ib the ligne_de_sortie list the name of the 2 sequences compared
		ligne_de_sortie.append(geno.name)
		ligne_de_sortie.append(haplo.name)
		for i in range(len(geno.sequence)) :
			#traitment of Hmz Markers
			if len(geno.sequence[i]) == 1 :
				if geno.sequence[i] == haplo.sequence[i] :
					ligne_de_sortie.append(0)
				else :
					ligne_de_sortie.append(1)
					count_erreur += 1
			#traitment of unknowing base for markers ('--')
			elif len(geno.sequence[i]) == 2 :
				ligne_de_sortie.append(0)
			#traitment of Htz markers
			elif len(geno.sequence[i]) == 3 :
				if geno.sequence[i].rsplit("/", 1)[0] != haplo.sequence[i] :
					if geno.sequence[i].rsplit("/", 1)[1] != haplo.sequence[i] :
						ligne_de_sortie.append(1)
						count_erreur += 1
					else :
						ligne_de_sortie.append(0)
				else :
					ligne_de_sortie.append(0)
		ligne_de_sortie.append(count_erreur)
		#print (len(ligne_de_sortie)) #--> need be equal to (len(markers) + geno.name(=1) + haplo.name(=1) + sum(count_erreur)(=1) so len(markers)+3)
		return ligne_de_sortie

#Need change, add threshold (default = 0) 
	def select_similar_haplotype(self, geno, haplo):
		"""Put in the similar_haplotype list the Haplotype object for which the last index
		of the compare_two_seq() return is equal to 0. it means that our haplotype can explain
		our genotype.

		Named parameters :
		geno -- The Genotype object 
		haplo -- The Haplotype object  

		"""
		#We look at the last index (sum of error between the 2 sequences) of the comparative list
		if geno.compare_two_seq(geno, haplo)[-1] == 0 :
			geno.similar_haplotype.append(haplo)
		else :
			pass

#Because of the change before
#Need accepte 2*thresold errors (but only at the error marker)
	def combinaison_between_similar_haplotype_in_geno(self):
		"""Return a list of 2 Haplotypes objects list or nothing (if it's the case).
		Which, if they are assembled, explain the observed genotype.

		"""
		#Use of the index_htz_markers_in_seq
		#Take care !!! unknow markers '--' considered like Htz markers in the index_htz_markers_in_seq list
		lstZip = []
		lst_good_combinaison = []
		if self.number_of_similar_haplotype > 1 :
			for haplo1, haplo2 in it.combinations(self.similar_haplotype, 2) :
				lst_combinaison = []
				lstZip = list(zip(haplo1.sequence, haplo2.sequence, self.sequence))
				count_bad_combinaison = 0
				for val_index in self.index_htz_markers_in_seq :
					#we only considered the real htz markers ('A/G')
					if len(lstZip[val_index][2]) == 3 : 
						tmp_bases_combine = lstZip[val_index][0] + "/" + lstZip[val_index][1]
						tmp_bases_combine2 = lstZip[val_index][1] + "/" + lstZip[val_index][0]
						if tmp_bases_combine == lstZip[val_index][2] or tmp_bases_combine2 == lstZip[val_index][2] :
							lst_combinaison.append(0)
						else :
							lst_combinaison.append(1)
							count_bad_combinaison += 1
				if count_bad_combinaison == 0 :
					lst_good_combinaison.append([haplo1, haplo2])
		return lst_good_combinaison
		#This list can be empty if any combination can explain our genotype

	def create_haplotype(self, haplotype, genotype):
		"""Return a list of a new haplotype sequence.
		Which is created by the asociation between a genotype and one of his similar haplotype.  

		Named parameters :
		haplotype -- The Haplotype object  
		genotype -- The Genotype object 

		"""
		new_haplotype = []
		#we compare each markers to have: 
		lstZip = list(zip(haplotype.sequence, genotype.sequence)) 
		for nt in range(len(genotype.sequence)) :
			#when it was a hmz markers, the same one
			if len(lstZip[nt][1]) == 1 :
				new_haplotype.append(lstZip[nt][0])
			#when it was a unknow, a unknow one
			if len(lstZip[nt][1]) == 2 :
				new_haplotype.append("--")
			#when it was a htz markers, the complementary one
			if len(lstZip[nt][1]) == 3 :
				if lstZip[nt][0] == lstZip[nt][1].rsplit("/",1)[0]:
					new_haplotype.append(lstZip[nt][1].rsplit("/",1)[1])
				if lstZip[nt][0] == lstZip[nt][1].rsplit("/",1)[1]:
					new_haplotype.append(lstZip[nt][1].rsplit("/",1)[0])
		return new_haplotype

	#trouver un autre nom a cette fonction
	def have_new_haplotype(self):
		"""Return a list of new haplotypes sequences for Genotypes objects who :
			-have a minimum of 1 similar haplotype
			-the combination of different similar haplotype can't explain the observed genotype

		"""
		lst_new_haplo = []
		if self.number_of_similar_haplotype == 0 :
			pass
		#Create a new haplotype for the genotype with a uniq similar haplotype
		if self.number_of_similar_haplotype == 1 :
			lst_new_haplo.append(self.create_haplotype(self.similar_haplotype[0], self))
		#And for the genotype who have similar haplotype but any of them have a good combination
		if self.number_of_similar_haplotype > 1 :
			if self.number_of_probable_haplotypes_combinaison == 0 :
				for haplo in self.similar_haplotype : 
					lst_new_haplo.append(self.create_haplotype(haplo, self)) #voir ici les bon argument a mettre (car haplotype = haplo et genotype = self)
			else : 
				pass

			#a try with the similar haplotype who stays when we have a good combination with the similar haplotype.
			#But it has no interest because a best is already known  
			"""if self.number_of_probable_haplotypes_combinaison > 0 :
				lst_simplifie = []
				for combi in self.probable_haplotypes_combinaison : # ex : [haplo1, haplo3] in [[haplo1,haplo3],[haplo1,haplo6]] ...
					for haplo_combi in combi : #pour haplo1 in [haplo1, haplo3] ...
						lst_simplifie.append(haplo_combi) #ce sont des objets ou des séquences directement?
					#Permet de passer de ce format ex: [[haplo1,haplo3],[haplo1,haplo6]] --> [haplo1, haplo3, haplo1, haplo6] (Plus facile ensuite pour récupérer les haplotypes qui ne combine pas)
				for haplo in self.similar_haplotype :
					if haplo not in lst_simplifie :
						lst_of_haplotype_who_is_not_combine.append(haplo)
					else :
						pass
				#print ("haplo sans combi {}".format(lst_of_haplotype_who_not_combine))

				for i in lst_of_haplotype_who_is_not_combine :
					lst_new_haplo.append(create_haplotype(i, lst3))""" #here .append the attribut containing the new haplotype list

		return lst_new_haplo