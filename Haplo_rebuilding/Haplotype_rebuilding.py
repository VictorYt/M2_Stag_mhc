#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Tout traduire en anglais
"""Programme de reconstruction d'haplotype 
..."""


#A faire
	#Gérer les options -i -o etc ...
	#Etape de filtrage (par défaut pas présente, ou si présente savoir quels individus on quel haplotype)
	#Script d'analyse des géno sur la base des Hmz
	#Sorties (brut/rangée/comme on souhaite les avoir/...)


#Nécessite de décrire le format d'inpu des 2 entrées.
#1 ouverture des fichiers et enregistrement dans des listes de haplo et génotype.

from csv import reader
from sys import argv

#haplotype = argv[1]
#genotype = argv[2]
#delimit = "\t"

class Haplotype(object):
	"""Classe définissant un Haplotype.
	Il est caractérisé par son nom, sa taille (nombre de marqueurs) et sa séquence"""
	def __init__(self, name, sequence):
		self._name = name 
		self._sequence = sequence 
		self._nbmarkers = len(self._sequence) #ou len(sequence)
		self._markers = "" #en-tête du fichier en input
		#Faire attention au fichier : utilisation du fichier d'haplotype pour les haplotypes et idem pour génotype
		#ça nous permettra de vérifier qu'on a bien les même SNP avant comparaison


	def __str__(self):
		"""Méthode permettant d'afficher notre Haplotype"""
		return "L'haplotype {}, construit à l'aide de {} marqueurs, est : {}".format(self._name, self._nbmarkers, self._sequence)


	#ACCESSEURS

	def _get_name(self):
		"""Méthode appelée si l'on souhaite accéder en lecture à l'attribut name"""
		#print("Le nom de l'haplotype est :")
		return self._name

	def _get_sequence(self):
		"""Méthode appelée si l'on souhaite accéder en lecture à l'attribut sequence"""
		#print ("La séquence de cet haplotype est :")
		return self._sequence

	def _get_nbmarkers(self):
		"""Méthode appelée si l'on souhaite accéder en lecture à l'attribut nbmarkers"""
		#print ("Le nombre de marqueurs est de :")
		return self._nbmarkers

	def _get_markers(self):
		"""Méthode appelée si l'on souhaite accéder en lecture à l'attribut markers"""
		return self._markers


	#MUTATEURS

	def _set_name (self, newname):
		"""Permet de récupérer le nom de notre haplotype
		Que prendre comme nom? (le mieux reste de le fournir en input = rows[0]"""
		#ici name rows[0]
		self._name = newname

	def _set_sequence(self, newsequence):
		"""Permet d'indiquer la sequence de l'haplotype aux marqueurs donnés
		Faire une autre fonction qui la récupère elle même"""
		self._sequence = sequence

	def _set_nbmarkers(self, newnbmarkers):
		"""Permet d'indiquer le nombre de marqueurs s'il est connu
		Faire une autre fonction ou il va le récupérer elle même"""
		self._nbmarkers = newnbmarkers

	def _set_markers(self):
		"""Permet de changer l'attribut indiquant la liste des marqueurs utilisé ici"""
		self._markers = # lui dire que c'est le header de mon fichier il ne comprendra pas ici


	#PROPERTIES

	name = property(_get_name, _set_name)
	nbmarkers = property(_get_nbmarkers, _set_nbmarkers)
	sequence = property(_get_sequence, _set_sequence)

	#OTHER METHODES

	def sequence_size(self):
		"""Permet de récupérer la taille de notre séquence 
		(cf. le nombre de marqueurs ayant servis pour le génotypage"""
		return len(self._sequence)
		#pas utile ici si je fais directement un len de ma variable dès le début











class Genotype(Haplotype):
	"""docstring for Genotype"""
	def __init__(self):
		self._nb_hmz_markers = 0
		self._nb_htz_markers = 0
		self._index_htz_markers_in_seq = [] #liste des positions Htz dans seq du genotype (rend plus rapide la comparaison entre haplo possiblement combiné pour donner seq du génotype)
		self._same_as_a_haplotype = same_as_a_haplotype #une liste de sequences (eux même des liste de caractères)
		self._number_of_same_as_a_haplotype = number_of_same_as_a_haplotype #taille de la liste obtenue ci-dessus
		self._probable_haplotype = probable_haplotype #si la taille calculé au dessus est de 1 recherche de l'haplotype qui combiné a celui trouvé donne notre génotype
		self._number_of_probable_haplotype = number_of_probable_haplotype


if __name__ == '__main__':
	haplo1 = Haplotype("SNP1", 79, "ATGC")
	haplo2 = Haplotype("SNP2", 79, "CTAG")
	print (haplo1)
	print (haplo2)
	print (haplo1.name)
	print (haplo2.sequence)
	#Pour le moment pas besoin de mes accesseurs et mutateurs



#Créer une liste d'haplotype comme ceci en lisant mon input haplotype
#parcourir ensuite cette liste juste sur l'attribut seq (Tout en connaissance l'attribut name pour le retourner quand la seq est très suimilaire à notre Haplotype)
# voir https://openclassrooms.com/courses/apprenez-a-programmer-en-python/parenthese-sur-le-tri-en-python


"""
with open(halpotype, 'r') as src :
		my_reader = reader(src, delimiter = delimit)
		
		for rows in my_reader :
			#Enregistrer les haplotypes dans des listes utilisées par la suite pour les comparaisons

			"""
#voir comment gérer un header