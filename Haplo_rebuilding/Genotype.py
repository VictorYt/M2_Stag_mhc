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
		self._hmz_nb_of_markers = 0
		self._htz_nb_of_markers = 0
		self._index_htz_markers = [] #liste des positions Htz dans seq du genotype (rend plus rapide la comparaison entre haplo possiblement combiné pour donner seq du génotype)
		
		#supp
		self._similar_haplotype = [] #une liste de sequences (eux même des liste de caractères)					 # = half_similarity hérité de Haplotype
		self._number_of_similar_haplotype = 0 #taille de la liste obtenue ci-dessus
		
		self._probable_haplotypes_combinaison = [] #liste de liste (ex: [[haplo1, haplo4], [haplo20, haplo79]])
		self._number_of_probable_haplotypes_combinaison = 0	
		self._lst_of_new_haplotype = [] #une liste de nouveau(x) (pour le moment liste de la séqeunce seul) haplotype(s) créé à partir de l'objet Génotype en question
		self._number_of_new_created_haplotype = 0 #taille de la liste obtenue ci-dessus
		self._probable_haplotypes_combinaison_2_run = [] # nouvelle liste de combinaison 
		self._number_of_probable_haplotypes_combinaison_2_run = 0

	def __str__(self):
		"""Like str Haplotype a quick description of our Genotype object"""
		return "Genotype {}, constructed using {} markers, is : {}".format(self._name, self._nbmarkers, self._sequence)


	############
	#ACCESSEURS#
	############

	def _get_hmz_nb_of_markers(self):
		"""Return the attribute that contains the number of Hmz markers"""
		return self._hmz_nb_of_markers

	def _get_htz_nb_of_markers(self):
		"""Return the attribute that contains the number of Htz markers"""
		return self._htz_nb_of_markers

	def _get_index_htz_markers(self):
		"""Return the attribute that contains a list with the indexs of Hmz markers"""
		return self._index_htz_markers
	
	#supp
	def _get_similar_haplotype(self):
		"""Return the attribute that contains a Haplotype object list  
		similar to our genotype

		"""
		return self._similar_haplotype#Va disparaitre pour half_similar_with hérité de la class Haplotype

	#supp
	def _get_number_of_similar_haplotype(self):
		"""Return the attribute that contains the size of the similar Haplotype object list"""
		return self._number_of_similar_haplotype#va être changer ou disparaitre

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

	def _set_hmz_nb_of_markers(self, hmz_nb_markers):
		"""Changes the number of Hmz markers in genotype

		Named parameters :
		hmz_nb_markers -- a int (default = 0)

		"""
		self._hmz_nb_of_markers = hmz_nb_markers

	def _set_htz_nb_of_markers(self, htz_nb_markers):
		"""Changes the number of Htz markers in genotype

		Named parameters :
		htz_nb_markers -- a int (default = 0)

		"""
		self._htz_nb_of_markers = htz_nb_markers

	def _set_index_htz_markers(self, index_htz_markers):
		"""Changes the list of Htz markers indexs in genotype

		Named parameters :
		index_htz_markers -- a list (empty by default)

		"""
		self._index_htz_markers = index_htz_markers

	#supp	
	def _set_similar_haplotype(self, similar_haplotype):
		"""Changes the list of similar haplotype with our genotype

		Named parameters :
		similar_haplotype -- a list (empty by default)

		"""
		self._similar_haplotype = similar_haplotype #Va disparaitre pour half_similar_with hérité de la class Haplotype

	#supp
	def _set_number_of_similar_haplotype(self, nb_similar_haplotype):
		"""Changes the number of similar haplotype with our genotype

		Named parameters :
		nb_similar_haplotype -- a int (default = 0)

		"""
		self._number_of_similar_haplotype = nb_similar_haplotype #va être changer ou disparaitre

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

	hmz_nb_of_markers = property(_get_hmz_nb_of_markers, _set_hmz_nb_of_markers)
	htz_nb_of_markers = property(_get_htz_nb_of_markers, _set_htz_nb_of_markers)
	index_htz_markers = property(_get_index_htz_markers, _set_index_htz_markers)
	
	#supp
	similar_haplotype = property(_get_similar_haplotype, _set_similar_haplotype) #va disparait pour être remplacer par la methode que je vais faire dans la class Haplotype
	#supp
	number_of_similar_haplotype = property(_get_number_of_similar_haplotype, _set_number_of_similar_haplotype) #probablement aussi celle-ci
	
	probable_haplotypes_combinaison = property(_get_probable_haplotypes_combinaison, _set_probable_haplotypes_combinaison) #un surchage de la methode que j'aurais dans la class haplotype
	number_of_probable_haplotypes_combinaison = property(_get_number_of_probable_haplotypes_combinaison, _set_number_of_probable_haplotypes_combinaison) #idem
	lst_of_new_haplotype = property(_get_lst_of_new_haplotype, _set_lst_of_new_haplotype) #modifié car va prendre les haplo avec 0 missmatch et aussi 1 et 2 et "coriger les fautes"
	number_of_new_created_haplotype = property(_get_number_of_new_created_haplotype, _set_number_of_new_created_haplotype)
	probable_haplotypes_combinaison_2_run = property(_get_probable_haplotypes_combinaison_2_run, _set_probable_haplotypes_combinaison_2_run)
	number_of_probable_haplotypes_combinaison_2_run = property(_get_number_of_probable_haplotypes_combinaison_2_run, _set_number_of_probable_haplotypes_combinaison_2_run)

	################
	#OTHER METHODES#
	################

	#CARE missing data (--) here is considered like a Htz 
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

	def have_nb_of_htz_markers(self):
		"""Return the number of Htz markers by checking the length of the list
		recovering by the function position_htz_markers()

		"""
		return len(self._index_htz_markers)

	def have_nb_of_hmz_markers(self):
		"""Return the number of Hmz markers by subtracting the total number of markers (_nbmarkers)
		with the number of Htz markers (find with have_nb_of_htz_markers())

		"""
		return self._nbmarkers - self._htz_nb_of_markers




#changement de la fonction pour quelle prenne en compte le threshold ==> OK
	def combinaison_between_compatible_haplotype_in_geno_test(self):
		"""Return a list of 2 Haplotypes objects list or nothing (if it's the case).
		Which, if they are assembled, explain the observed genotype.

		"""
		#Use of the index_htz_markers
		#Take care !!! unknow markers '--' considered like Htz markers in the index_htz_markers list
		lstZip = []
		lst_good_combinaison = []
		#I only combine the haplotype with 
		if len(self.half_similarity_with[0]) > 1 :
			for haplo1, haplo2 in it.combinations(self.half_similarity_with[0], 2) :
				lst_combinaison = []
				lstZip = list(zip(haplo1.sequence, haplo2.sequence, self.sequence))
				count_bad_combinaison = 0
				for val_index in self.index_htz_markers :
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

#changer ou créer une autre pour les haplotype avec erreurs ==> OK
	def create_haplotype_test(self, haplotype):#donner le lnom "create_haplotype_seq"
		"""Return a list of a new haplotype sequence.
		Which is created by the asociation between a genotype and one of his similar haplotype.  

		Named parameters :
		haplotype -- The Haplotype object  

		"""
		new_haplotype = []
		#we compare each markers to have: 
		lstZip = list(zip(haplotype.sequence, self.sequence)) 
		for nt in range(len(self.sequence)) :
			#when it was a hmz markers, the same one
			if len(lstZip[nt][1]) == 1 :
				new_haplotype.append(lstZip[nt][1])########################Je ne fait pas attention s'il y a 1 ou plus d'erreur ici (car erreur ne peut être que sur Hmz SNP)
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

#fonction du dessous mieux (a delete)
	def have_new_haplotype_test(self):
		"""Return a list of new haplotypes sequences for Genotypes objects who :
			-have a minimum of 1 similar haplotype
			-the combination of different similar haplotype can't explain the observed genotype

		"""
		lst_new_haplo = []
		#I run all my dico.keys() heure
		for i in self.half_similarity_with.keys() :
			#i create haplotype only if my Genotype isn't confirmed by 2 Known Haplotypes
			if self.number_of_probable_haplotypes_combinaison == 0 :
				#Create a new haplotype for the genotype with a uniq similar haplotype
				if len(self.half_similarity_with[i]) == 1 :
					lst_new_haplo.append(self.create_haplotype_test(self.half_similarity_with[i][0]))
				#And for the genotype who have similar haplotype but any of them have a good combination
				elif len(self.half_similarity_with[i]) > 1 :
					if self.number_of_probable_haplotypes_combinaison == 0 :
						for haplo in self.half_similarity_with[i] : 
							lst_new_haplo.append(self.create_haplotype_test(haplo)) 
					else : #because i already have a strong combination with Known Haplotypes
						pass

		return lst_new_haplo
		#just a list for now, like that i lose the correct haplo

#a concerver ===>OK
	def have_new_haplotype_test_better(self):
		"""Return a list of new haplotypes instances for Genotypes objects who :
			-have a minimum of 1 half_similar Haplotype,
			-the combination between similar haplotype can't explain the observed genotype.

		"""
		lst_new_haplo = []
		#I run all my dico.keys() heure
		for i in self.half_similarity_with.keys() :
			#i create haplotype only if my Genotype isn't confirmed by 2 Known Haplotypes
			if self.number_of_probable_haplotypes_combinaison == 0 :
				for haplo in self.half_similarity_with[i] :
					candidate_name = "New:{}//{}".format(self.name, haplo.name)
					candidate_seq =  self.create_haplotype_test(haplo)
					candidate_markers = self.markers
					C = Haplotype(name=candidate_name, sequence=candidate_seq, markers=candidate_markers)
					lst_new_haplo.append(C)
		return lst_new_haplo 


