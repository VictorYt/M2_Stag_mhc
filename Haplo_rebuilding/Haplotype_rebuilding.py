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

haplotype = argv[1]
delimit = "\t"

class Haplotype:
	"""Classe définissant un Haplotype.
	Il est caractérisé par son nom, sa taille (nombre de marqueurs) et sa séquence"""
	def __init__(self, name = "", nbmarkers = "", sequence = ""):
		self.name = name 
		self.nbmarkers = nbmarkers 
		self.sequence = sequence 
		#vide pour le moment

	def __str__(self):
		"""Méthode permettant d'afficher notre Haplotype"""
		return "L'haplotype {}, construit à l'aide de {} marqueurs est : ".format(self.name, self.nbmarkers, self.sequence)

	def getName(self):
		"""Méthode appelée si l'on souhaite accéder en lecture à l'attribut name"""
		print("Le nom de l'haplotype est :")
		return self.name

	def getNumberOfMarkers(self):
		"""Méthode appelée si l'on souhaite accéder en lecture à l'attribut nbmarkers"""
		print ("Le nombre de marqueurs est de :")
		return self.nbmarkers

	def getSequence(self):
		"""Méthode appelée si l'on souhaite accéder en lecture à l'attribut sequence"""
		print ("La séquence de cet haplotype est :")
		return self.sequence



	def setName (self, name):
		"""Permet de récupérer le nom de notre haplotype
		Que prendre comme nom? (le mieux reste de le fournir en input = rows[0]"""
		#ici name rows[0]
		return self.name = name

	def setNumberOfMarkers(self, nbmarkers):
		"""Permet d'indiquer le nombre de marqueurs s'il est connu
		Faire une autre fonction ou il va le récupérer elle même"""
		return self.nbmarkers = nbmarkers

	def setSequence(self, sequence):
		"""Permet d'indiquer la sequence de l'haplotype aux marqueurs donnés
		Faire une autre fonction qui la récupère elle même"""
		return self.sequence = sequence


#Con mais je sais pas si faire une classe est interessante ici ou pas.
#créer une méthode .seq() qui renvérai la sequence d'un haplotype




class Genotype(Haplotype):
	"""docstring for Genotype"""
	def __init__(self, same_as_a_haplotype = list(), number_of_same_as_a_haplotype = int(), probable_haplotype = list()):
		self.same_as_a_haplotype = same_as_a_haplotype #une liste de sequences (eux même des liste de caractères)
		self.number_of_same_as_a_haplotype = number_of_same_as_a_haplotype #taille de la liste obtenue ci-dessus
		self.probable_haplotype = probable_haplotype #si la taille calculé au dessus est de 1 recherche de l'haplotype qui combiné a celui trouvé donne notre génotype
if


 __name__ == '__main__':
	test = Haplotype("SNP1", 79,"ATGC")


"""
with open(halpotype, 'r') as src :
		my_reader = reader(src, delimiter = delimit)
		
		for rows in my_reader :
			#Enregistrer les haplotypes dans des listes utilisées par la suite pour les comparaisons

			"""