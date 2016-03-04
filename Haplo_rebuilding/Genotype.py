#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Haplotype import Haplotype

class Genotype(Haplotype):
	"""docstring for Genotype"""
	def __init__(self, name, sequence, markers):
		#héritage de la classe Haplotype
		Haplotype.__init__(self, name, sequence, markers)
		#Propre à la classe Génotype
		self._nb_hmz_markers = 0
		self._nb_htz_markers = 0
		self._index_htz_markers_in_seq = [] #liste des positions Htz dans seq du genotype (rend plus rapide la comparaison entre haplo possiblement combiné pour donner seq du génotype)
		self._similar_haplotype = [] #une liste de sequences (eux même des liste de caractères)
		self._number_of_similar_haplotype = 0 #taille de la liste obtenue ci-dessus
		self._probable_haplotypes_combinaison = [] #liste de liste (ex: [[haplo1, haplo4], [haplo20, haplo79]])
		self._number_of_probable_haplotypes_combinaison = 0
		self._lst_of_new_haplotype = [] #une liste de nouveau(x) (pour le moment liste de la séqeunce seul) haplotype(s) créé à partir de l'objet Génotype en question
		self._number_of_new_created_haplotype = 0 #taille de la liste obtenue ci-dessus

	def __str__(self):
		"""Like str Haplotype"""
		return "Le Genotype {}, construit à l'aide de {} marqueurs, est : {}".format(self._name, self._nbmarkers, self._sequence)


	############
	#ACCESSEURS#
	############

	def _get_nb_hmz_markers(self):
		"""Permet d'avoir accès au nombre de markers Hmz dans le génotype"""
		return self._nb_hmz_markers

	def _get_nb_htz_markers(self):
		"""Permet d'avoir accès au nombre de markers Htz dans le génotype"""
		return self._nb_htz_markers

	def _get_index_htz_markers_in_seq(self):
		"""Permet d'avoir les indexes des positions ou le markers génotypique est Htz"""
		return self._index_htz_markers_in_seq
	
	def _get_similar_haplotype(self):
		"""Permet d'avoir la liste des objets Hapltype qui ont une séquence
		compatible avec notre génotype"""
		return self._similar_haplotype

	def _get_number_of_similar_haplotype(self):
		"""Permet d'avoir le nombre d'hapltype contenu dans la liste d'haplotype similaire"""
		return self._number_of_similar_haplotype

	def _get_probable_haplotypes_combinaison(self):
		"""Permet d'avoir une liste de combinaison de 2 haplotypes donnant le génotype observé"""
		return self._probable_haplotypes_combinaison

	def _get_number_of_probable_haplotypes_combinaison(self):
		"""Permet d'avoir le nombre de combinaison contenu dans la liste de combinaison probable"""
		return self._number_of_probable_haplotypes_combinaison		

	def _get_lst_of_new_haplotype(self):
		"""Permet d'avoir la liste des nouveaux haplotypes créés"""
		return self._lst_of_new_haplotype

	def _get_number_of_new_created_haplotype(self):
		"""Permet d'avoir le nombre de nouveaux haplotypes créés"""
		return self._number_of_new_created_haplotype

	###########
	#MUTATEURS#
	###########

	def _set_nb_hmz_markers(self, nb_hmz_markers):
		"""Permet de changer accès au nombre de markers Hmz dans le génotype"""
		self._nb_hmz_markers = nb_hmz_markers

	def _set_nb_htz_markers(self, nb_htz_markers):
		"""Permet de changer accès au nombre de markers Htz dans le génotype"""
		self._nb_htz_markers = nb_htz_markers

	def _set_index_htz_markers_in_seq(self, index_htz_markers):
		"""Permet de changer les indexes des positions ou le markers génotypique est Htz"""
		self._index_htz_markers_in_seq = index_htz_markers
	
	def _set_similar_haplotype(self, similar_haplotype):
		"""Permet de changer la liste des objets Hapltype qui ont une séquence
		compatible avec notre génotype"""
		self._similar_haplotype = similar_haplotype

	def _set_number_of_similar_haplotype(self, nb_similar_haplotype):
		"""Permet de changer le nombre d'hapltype contenu dans la liste d'haplotype similaire"""
		self._number_of_similar_haplotype = nb_similar_haplotype

	def _set_probable_haplotypes_combinaison(self, haplo_combinaison):
		"""Permet de changer une liste de combinaison de 2 haplotypes donnant le génotype observé"""
		self._probable_haplotypes_combinaison = haplo_combinaison

	def _set_number_of_probable_haplotypes_combinaison(self, nb_haplo_combinaison):
		"""Permet de changer le nombre de combinaison contenu dans la liste de combinaison probable"""
		self._number_of_probable_haplotypes_combinaison = nb_haplo_combinaison

	def _set_lst_of_new_haplotype(self, new_haplotype):
		"""Permet de changer la liste des haplotypes créé, qui est initialement vide, 
		par celle générée par la méthode create_haplotype()"""
		self._lst_of_new_haplotype = new_haplotype

	def _set_number_of_new_created_haplotype(self, new_number):
		"""Permet de changer le nombre de nouveau(x) haplotype(s), qui est initialement
		de zéro, au nombre réel de nouveau(x) haplotype(s) créé(s)"""
		self._number_of_new_created_haplotype = new_number

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

	################
	#OTHER METHODES#
	################

	#attention je prend en compte les erreur de calling (--) dans le compte des Htz
	#erreur d'indexation ===> a corriger
	def position_htz_markers(self):
		"""Permet de retourner une liste de position (index pour lesquels le markers est Htz)"""
		position_htz_markers = []
		for nt in range(len(self.sequence)) : 
			if len(self.sequence[nt]) > 1 :
				position_htz_markers.append(nt)
			else :
				pass
		return position_htz_markers

	def have_nb_htz_markers(self):
		"""Permet d'avoir le nombre de markers Htz"""
		return len(self._index_htz_markers_in_seq)

	def have_nb_hmz_markers(self):
		"""Permet d'avoir le nombre de marqueurs Hmz en faisant 
		la soustraction du nombre de markers moins le nombre de htz trouvé"""
		return self._nbmarkers - self._nb_htz_markers #créer une branche pour gérer les -- (pas Htz mais markers non connu)

	def compare_geno_and_haplo_seq(self, geno, haplo):
		"""Permet de comparer une sequence d'un genotype avec la séquence d'un halpotype
		Return une liste contenant le nom du genotype, le nom de l'haplotype, une séquence où : 
		0 = match entre génotype et haplotype
		1 = missmatch
		Et la dernière valeur étant un SUM des missmatch"""
		ligne_de_sortie = []
		count_erreur = 0
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
			#traitment of unknowing base for markers
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
		#print (len(ligne_de_sortie)) #--> need be equal to 82 (=79 markers + geno.name + heplo.name + sum(count_erreur))
		return ligne_de_sortie

	def select_similar_haplotype(self, geno, haplo):
		"""Permet de récupérer l'objet haplotype qui est parfaitement similaire au génotype
		Dont la somme des erreurs réaliser avec la méthode compare_geno_and_haplo_seq = 0 """
		if geno.compare_geno_and_haplo_seq(geno, haplo)[81] == 0 :
			geno.similar_haplotype.append(haplo)
		else :
			pass

	def combinaison_between_similar_haplotype_in_geno(self):
		"""Permet de combiner 1 à 1 les haplotypes précédemment trouvé pour vérifier
		si notre génotype est issu de la combinaison d'haplotyes déjà connu"""
		#utilisation de la liste d'index des marqueurs Htz chez le génotype
		#faire attention ... pour le moment -- concidéré comme Htz dans le nb Htz/Hmz donc certain index pointe vers --
		lstZip = []
		lst_good_combinaison = []
		if self.number_of_similar_haplotype > 1 :
			for haplo1 in range(len(self.similar_haplotype)-1) :
				for haplo2 in range((haplo1+1),len(self.similar_haplotype)) :
					lst_combinaison = []
					lstZip = list(zip((self.similar_haplotype[haplo1]).sequence, (self.similar_haplotype[haplo2]).sequence, self.sequence))
					count_bad_combinaison = 0
					for val_index in self.index_htz_markers_in_seq :
						if len(lstZip[val_index][2]) == 3 : 
							tmp_bases_combine = lstZip[val_index][0] + "/" + lstZip[val_index][1]
							tmp_bases_combine2 = lstZip[val_index][1] + "/" + lstZip[val_index][0]
							if tmp_bases_combine == lstZip[val_index][2] or tmp_bases_combine2 == lstZip[val_index][2] :
								lst_combinaison.append(0)
							else :
								lst_combinaison.append(1)
								count_bad_combinaison += 1
					if count_bad_combinaison == 0 :
						lst_good_combinaison.append([self.similar_haplotype[haplo1].name, self.similar_haplotype[haplo2].name])		
		return lst_good_combinaison
		#Cette liste peut être vide
		#Prendre en compte ce cas
		#Ainsi que les haplotype qui combiné ne donne rien (len(self.similar_haplotype) - len(lst_good_combinaison))

	#Les arguments (haplotype et genotype ici) sont des objets
	def create_haplotype(self, haplotype, genotype):
		"""Permet, à partir d'un génotype et d'un haplotype de reconstruire l'haplotype manquant,
		qui combiné à celui connu donne le génotype connu """
		new_haplotype = []
		#comme les arguments sont des objets on peut utiliser la méthode .sequence pour avoir la séquence
		lstZip = list(zip(haplotype.sequence, genotype.sequence)) 
		for nt in range(len(genotype.sequence)) :
			if len(lstZip[nt][1]) == 1 :
				new_haplotype.append(lstZip[nt][0])
			if len(lstZip[nt][1]) == 2 :
				new_haplotype.append("--")
			if len(lstZip[nt][1]) == 3 :
				if lstZip[nt][0] == lstZip[nt][1].rsplit("/",1)[0]:
					new_haplotype.append(lstZip[nt][1].rsplit("/",1)[1])
				if lstZip[nt][0] == lstZip[nt][1].rsplit("/",1)[1]:
					new_haplotype.append(lstZip[nt][1].rsplit("/",1)[0])
		return new_haplotype

	#trouver un autre nom a cette fonction
	def have_new_haplotype(self):
		"""Permet, de créer un nouvel haplotype avec tous les génotypes ayant au moins 1 haplotype similaire
		,lequel ne combinant pas avec un autre halpotype similaire, pour donner le génotype observé"""
		lst_new_haplo = []
		if self.number_of_similar_haplotype == 0 :
			pass
		#creattion d'un nouveau haplotype si 1 seul haplotype connu retrouvé comme commun à notre génotype
		if self.number_of_similar_haplotype == 1 :
			lst_new_haplo.append(self.create_haplotype(self.similar_haplotype[0], self))
		if self.number_of_similar_haplotype > 1 :
			if self.number_of_probable_haplotypes_combinaison == 0 :
				for haplo in self.similar_haplotype : 
					lst_new_haplo.append(self.create_haplotype(haplo, self)) #voir ici les bon argument a mettre (car haplotype = haplo et genotype = self)
			else : 
				pass

			# Le cas ci-dessous n'est pas a prendre en compte car on obtient déjà une autre combinaison (avec des haplotypes connu), donc plus sûre
			#Il consistait, à partir de cronstruire les haplotypes
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
					lst_new_haplo.append(create_haplotype(i, lst3))""" #ici .append l'attribut contenant la liste des nvx haplo

		return lst_new_haplo