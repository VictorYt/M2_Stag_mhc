#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Tout traduire en anglais
"""Programme de reconstruction d'haplotype 
..."""


#A faire
	#Gérer les options -i -o etc ...
	#Etape de filtrage (par défaut pas présente, ou si présente savoir quels individus on quel haplotype)
	#Script d'analyse des géno sur la base des Hmz (methodes dans objet geno)
	#Sorties (brut/rangée/comme on souhaite les avoir/...)


#Nécessite de décrire le format d'input des 2 entrées.
#1 ouverture des fichiers et enregistrement dans des listes des objets haplo et génotype.

from csv import reader
from sys import argv
#voir le module imap interateur pour combinaison de liste


class Haplotype(object):
	"""Classe définissant un Haplotype.
	Il est caractérisé par son nom, sa taille (nombre de marqueurs) et sa séquence"""
	def __init__(self, name, sequence, markers):
		self._name = name 
		self._sequence = sequence 
		self._nbmarkers = len(self._sequence) #0 à création puis modif ou directe len(sequence)
		self._markers = markers #en-tête du fichier en input
		#Faire attention au fichier : utilisation du fichier d'haplotype pour les haplotypes et idem pour génotype
		#ça nous permettra de vérifier qu'on a bien les même SNP avant comparaison


	def __str__(self):
		"""Méthode permettant d'afficher notre Haplotype"""
		return "L'haplotype {}, construit à l'aide de {} marqueurs, est : {}".format(self._name, self._nbmarkers, self._sequence)

	############
	#ACCESSEURS#
	############

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

	###########
	#MUTATEURS#
	###########

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

	def _set_markers(self, lstmarkers):
		"""Permet de changer l'attribut indiquant la liste des marqueurs utilisé ici"""
		self._markers = lstmarkers # lui dire que c'est le header de mon fichier il ne comprendra pas ici

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

	def sequence_size(self):
		"""Permet de récupérer la taille de notre séquence 
		(cf. le nombre de marqueurs ayant servis pour le génotypage
		pour vérifier s'il est égale à notre nombre de marqueurs"""
		return len(self._markers)
		#pas utile ici si je fais directement un len de ma variable dès le début

	def markers_lst(self):
		"""Permet de récupérer le header de nos fichiers d'INPUT qui contient
		le nom de chacun des marqueurs"""
		#pas a mettre dans la classe
		pass

	def compare_markers_size(self):
		"""Permet de vérifier que tous les haplotypes ont le même nombre de markers
		Normalement pas de problème"""
		#pas a mettre dans la classe
		pass








class Genotype(Haplotype):
	"""docstring for Genotype"""
	def __init__(self, name, sequence, markers):
		self._name = name 
		self._sequence = sequence 
		self._nbmarkers = len(self._sequence) #0 à création puis modif ou directe len(sequence)
		self._markers = markers
		self._nb_hmz_markers = 0
		self._nb_htz_markers = 0
		self._index_htz_markers_in_seq = [] #liste des positions Htz dans seq du genotype (rend plus rapide la comparaison entre haplo possiblement combiné pour donner seq du génotype)
		self._similar_haplotype = [] #une liste de sequences (eux même des liste de caractères)
		self._number_of_similar_haplotype = 0 #taille de la liste obtenue ci-dessus
		self._probable_haplotypes_combinaison = [] #liste de liste (ex: [[haplo1, haplo4], [haplo20, haplo79]])
		self._number_of_probable_haplotypes_combinaison = 0


	def __str__(self):
		return "L'haplotype {}, construit à l'aide de {} marqueurs, est : {}".format(self._name, self._nbmarkers, self._sequence)


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


	################
	#OTHER METHODES#
	################

	def position_htz_markers(self):
		"""Permet de retourner une liste de position (index pour lesquels le markers est Htz)"""
		position_htz_markers = []
		for nt in self._sequence : 
			if len(nt) > 1 :
				position_htz_markers.append(self.sequence.index(nt))
			else :
				pass
		return position_htz_markers

	def have_nb_htz_markers(self):
		"""Permet d'avoir le nombre de markers Htz"""
		return len(self._index_htz_markers_in_seq)

	def have_nb_hmz_markers(self):
		"""Permet d'avoir le nombre de marqueurs Hmz en faisant 
		la soustraction du nombre de markers moins le nombre de htz trouvé"""
		return self._nbmarkers - self._nb_htz_markers


	def have_commun_haplotype(self):
		"""Permet de récupérer la 1ère sortie que je veux
		0 match
		1 missmatch
		sum des missmatch
		sélection des haplotyê where sum =0"""
		#me retroune la ligne de sortie voulu
		pass





	def screening(self):
		"""Permet de vérifier parmi les autres objets Genotype s'il y a des
		sequence identique à l'object geno que je manipule."""
		#Dans la class ou a l'exterieur? surement a l'exterieur
		pass





#main test
if __name__ == '__main__':
	haplo1 = Haplotype("Hmz1", ["A","T","G","C"], ["SNP2","SNP7", "SNP88", "SNP178"])
	haplo2 = Haplotype("Hmz2", ["C","T","A","G"], ["SNP2","SNP7", "SNP88", "SNP178"])
	geno1 = Genotype("Geno1", ["C/A","T","A/G","C/G"], ["SNP2","SNP7", "SNP88", "SNP178"])
	print (haplo1)
	print (haplo2)
	print (geno1)
	#ligne pour avoir une liste des positions de mes marqueurs Htz dans la séquence d'un objet geno
	geno1.index_htz_markers_in_seq = (geno1.position_htz_markers())
	#ligne pour set le nombre de marqueures htz
	geno1.nb_htz_markers = geno1.have_nb_htz_markers()
	print (haplo1.name)
	print (haplo2.sequence)
	print (geno1.sequence)
	print (geno1.index_htz_markers_in_seq)
	print (geno1.nbmarkers)
	print (geno1.nb_htz_markers)
	print (len(geno1.index_htz_markers_in_seq))
	#ligne pour set le nombre de marqueures hmz
	geno1.nb_hmz_markers = geno1.have_nb_hmz_markers()
	#boucler sur les tous les objets géno.. dans ma liste de géno (voir comment traiter le cas des géno redondants)
	print (geno1._nb_hmz_markers)



#Créer une liste d'haplotype comme ceci en lisant mon input haplotype
	#créer les input
#parcourir ensuite cette liste juste sur l'attribut seq (Tout en connaissance l'attribut name pour le retourner quand la seq est très suimilaire à notre Haplotype)
# voir https://openclassrooms.com/courses/apprenez-a-programmer-en-python/parenthese-sur-le-tri-en-python


"""
with open(halpotype, 'r') as src :
		my_reader = reader(src, delimiter = delimit)
		
		for rows in my_reader :
			#Enregistrer les haplotypes dans des listes utilisées par la suite pour les comparaisons

			"""
#voir comment gérer un header