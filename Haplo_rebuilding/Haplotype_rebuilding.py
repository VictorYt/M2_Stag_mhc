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

from csv import reader, writer
from sys import argv
#voir le module imap interateur pour combinaison de liste


class Haplotype(object):
	"""Classe définissant un Haplotype.
	Il est caractérisé par son nom, sa taille (nombre de marqueurs) et sa séquence"""
	def __init__(self, name, sequence, markers):
		self._name = name 
		self._sequence = sequence 
		self._nbmarkers = len(self._sequence) #0 à création puis modif avec len(self.markers) ou directe len(sequence)
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

	def compare_markers_and_sequence_size(self):
		"""Permet de vérifier que tous les haplotypes ont le même nombre de markers
		Normalement pas de problème"""
		if len(self._sequence) == self._nbmarkers :
			return True 
		else :
			return False
		#Voir comment la coder autrement
		#








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

	#attention je prend en compte les erreur de calling (--) dans le compte des Htz
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

	#A modifier légèrement si creation d'haplotype réaliser aussi sur autres que les génotypes avec 1 génotype similaire
	def create_haplotype(self):
		"""Permet, dans le cas ou 1 seul haplotype connu est trouvé compatible à notre génotype,
		de créer l'haplotype qui combiné a celui trouvé donne notre génotype """
		new_hapltype = []
		lstZip = []
		for nt in range(len(self.sequence)) :
			lstZip = list(zip((self.similar_haplotype)[0].sequence, self.sequence)) #pb d'attribu ici
			if len(lstZip[nt][1]) == 1 :
				new_hapltype.append(lstZip[nt][0])
			if len(lstZip[nt][1]) == 2 :
				new_hapltype.append("--")
			if len(lstZip[nt][1]) == 3 :
				if lstZip[nt][0] == lstZip[nt][1].rsplit("/",1)[0]:
					new_hapltype.append(lstZip[nt][1].rsplit("/",1)[1])
				if lstZip[nt][0] == lstZip[nt][1].rsplit("/",1)[1]:
					new_hapltype.append(lstZip[nt][1].rsplit("/",1)[0])
		return new_hapltype
		#Penser a conserver ce retour dans un attribut


	#Penser à une étape de "filtrage" vérifier si séquence génomique pas redondante
	def screening(self):
		"""Permet de vérifier parmi les autres objets Genotype s'il y a des
		sequence identique à l'object geno que je manipule."""
		#Dans la classe ou à l'exterieur? surement a l'exterieur (sort -u)
		pass







"""Création de 2 listes d'objets
La premire, lst_of_haplo_object, contient les n objets Haplotype
La seconde, lst_of_geno_object, contient les n objets Genotype"""

if __name__ == '__main__':
	print ("\nLes histoires commencent  :")
	lst_of_haplo_object = []
	lst_of_geno_object = []
	lst_markers_haplo = None
	lst_markers_geno = None
	delimit = "\t"
	haplotype = argv[1]
	genotype = argv[2]
	first_output = argv[3]
	second_output = argv[4]
	first_txt_output = argv[5]

	with open(haplotype, 'r') as src_haplo, open(genotype, 'r') as src_geno :
		my_haplo_reader = reader(src_haplo, delimiter = delimit)
		my_geno_reader = reader(src_geno, delimiter = ",")
		#my_otp1_writer = writer(otp1, delimiter = delimit)

		#Compteur utilisé pour la récupération du header
		count1 = 0
		count2 = 0

		"""Construction de ma lst_of_haplo_object"""
		for rows in my_haplo_reader :
			count1 += 1
			if count1 == 1 :
				lst_markers_haplo = rows[1:80]
			else :
				A = Haplotype(name = rows[0], sequence = rows[1:80], markers = lst_markers_haplo)
				lst_of_haplo_object.append(A)
		#print ("Nombre d'objet haplo :",len(lst_of_haplo_object))


		""" Construction de ma lst_of_geno_object"""
		for rows in my_geno_reader :
			count2 +=1
			if count2 == 1 :
				lst_markers_geno = rows[1:80]
			else :
				B = Genotype(name = rows[0], sequence = rows[1:80], markers = lst_markers_geno)
				lst_of_geno_object.append(B)
		#print ("Nombre d'objet geno :",len(lst_of_geno_object))



		"""Récupératoin du nombre de markers Hmz et Htz par génotype avec en plus l'index des position Htz"""
		print ("Les marqueurs des genotypes sont {}:".format(lst_of_geno_object[1].markers))
		for geno in lst_of_geno_object :
			#print ("Le genotype {}, constitué de {} marqueurs, à pour sequence \n{}".format(geno.name, geno.nbmarkers, geno.sequence))
			geno.index_htz_markers_in_seq = (geno.position_htz_markers())
			geno.nb_htz_markers = geno.have_nb_htz_markers()
			geno.nb_hmz_markers = geno.have_nb_hmz_markers()
			#print ("il a {} marqueurs Hmz et {} Htz".format(geno.nb_hmz_markers, geno.nb_htz_markers))



#Au lieu d'avoir 2 truc qui font quasiment la même chose, fait une fonction qui rempli tes objects.


		src_haplo.close()
		src_geno.close()



#A partir d'ici j'ai Ma liste d'Haplo et de Geno
	#voir pour interprétation des unknowing markers (new branche in git) va se traiter comme A/B sauf que là tout le temps = 0 ici tout le temps =0
	"""Comparaison 1 par 1 des génotype avec la liste des haplotype"""




	#ouverture des fichiers pour les 2 premières sorties
	with open(first_output, 'w') as otp1, open(second_output, 'w') as otp2 :
		my_otp1_writer = writer(otp1, delimiter = delimit)
		my_otp2_writer = writer(otp2, delimiter = delimit)

		

		for geno in lst_of_geno_object :
			for haplo in lst_of_haplo_object :
				geno.select_similar_haplotype(geno, haplo)
				geno.number_of_similar_haplotype = len(geno.similar_haplotype)

				#écriture de la première sortie
				my_otp1_writer.writerow(geno.compare_geno_and_haplo_seq(geno, haplo))

		otp1.close()



		#écriture de la seconde sortie (à revoir pas clair à la lecture)
		lst_header =[]
		lst_header.append("Genotype")
		lst_header.append("Haplotype")	
		for markers in lst_of_geno_object[0].markers :
			lst_header.append(markers)
		my_otp2_writer.writerow(lst_header)


		for geno in lst_of_geno_object:
			geno_second_sortie = []
			geno_second_sortie.append(geno.name)
			geno_second_sortie.append(geno.number_of_similar_haplotype)
			for values in geno.sequence :
				geno_second_sortie.append(values)
			my_otp2_writer.writerow(geno_second_sortie)

			
			if geno.number_of_similar_haplotype > 0 :
				for similar_haplo in geno.similar_haplotype :
					haplo_second_sortie = []
					haplo_second_sortie.append(geno.name)
					haplo_second_sortie.append(similar_haplo.name)
					for values in similar_haplo.sequence :
						haplo_second_sortie.append(values)
					my_otp2_writer.writerow(haplo_second_sortie)
				my_otp2_writer.writerow("\n")
			else : 
				my_otp2_writer.writerow("\n")
			
		otp2.close()


#fonction a décrire
#Voir pour inteégré dans la sortie txt
def count_genotype_with_same_number_of_similar_haplotype(genotype, theNumber) :
	"""theNumber a int between 0 to len(list_of_genotype_object)
	count is a counter that will be retrun"""
	if genotype.number_of_similar_haplotype == theNumber:
		count = 1
	else :
		count = 0
	return count

count_geno = 0
count = 0

for i in range((len(lst_of_haplo_object)+1)) :
	count_geno += count
	count = 0
	for geno in lst_of_geno_object :
		count += count_genotype_with_same_number_of_similar_haplotype(genotype =geno, theNumber =i)
	if count_geno < len(lst_of_geno_object) :		
		print ("Les genotypes avec {} haplotype(s) commun(s) sont au nombre de {}".format(i, count))

























"""Manip permettant d'avoir le nombre de combinaison viable en fonction du nombre d'haplotype possible"""

#Création de nouveaux haplotypes a partir des génotypes ayant qu'un haplotypes simailaire
	#penser a créer un attribut pour stocker la séquqence, voir de créer un nouveau objet Haplotype (plus clair et sérieux)
	#Voir pour le faire avec les génotypes avec plusieurs haplotypes similaires dont aucune combinaison fonctionne.
for geno in lst_of_geno_object :
	print ("Pour le genotype {}".format(geno.name))
	print ("Le nombre d'haplotype similaire a notre génotype est au nombre de : {}".format(geno.number_of_similar_haplotype))
	geno.probable_haplotypes_combinaison = geno.combinaison_between_similar_haplotype_in_geno()
	geno.number_of_probable_haplotypes_combinaison = len(geno.probable_haplotypes_combinaison)
	if geno.number_of_similar_haplotype == 1 :
		#Penser a créer un attribut pour concervé les haplotypes créé
		print ("L'haplotype manquant pour avoir le génotype serait :\n{}".format(geno.create_haplotype()))





























#Penser a faire une fonction qui pourrait me donner ces résultats
count_2_0 = 0
count_2_1 = 0

count_3_0 = 0
count_3_1 = 0
count_3_2 = 0
count_3_3 = 0

count_4_0 = 0
count_4_1 = 0
count_4_2 = 0

count_5_0 = 0
count_5_1 = 0

count_6_0 = 0
count_6_3 = 0


for geno in lst_of_geno_object :
	if geno.number_of_similar_haplotype == 2 : 
		if geno.number_of_probable_haplotypes_combinaison == 0 :
			count_2_0 += 1
		elif geno.number_of_probable_haplotypes_combinaison == 1 :
			count_2_1 +=1
	
	elif geno.number_of_similar_haplotype == 3 :
		if geno.number_of_probable_haplotypes_combinaison == 0 :
			count_3_0 += 1
		elif geno.number_of_probable_haplotypes_combinaison == 1 :
			count_3_1 +=1
		elif geno.number_of_probable_haplotypes_combinaison == 2 :
			count_3_2 += 1
		elif geno.number_of_probable_haplotypes_combinaison == 3 :
			count_3_3 += 1
	
	elif geno.number_of_similar_haplotype == 4 :
		if geno.number_of_probable_haplotypes_combinaison == 0 :
			count_4_0 += 1
		elif geno.number_of_probable_haplotypes_combinaison == 1 :
			count_4_1 +=1
		elif geno.number_of_probable_haplotypes_combinaison == 2 :
			count_4_2 += 1

	elif geno.number_of_similar_haplotype == 5 :
		if geno.number_of_probable_haplotypes_combinaison == 0 :
			count_5_0 += 1
		elif geno.number_of_probable_haplotypes_combinaison == 1 :
			count_5_1 +=1

	elif geno.number_of_similar_haplotype == 6 :
		if geno.number_of_probable_haplotypes_combinaison == 0 :
			count_6_0 += 1
		elif geno.number_of_probable_haplotypes_combinaison == 3 :
			count_6_3 += 1

print ("\n\nSi 2 haplotypes similaires au géno :\n{} ne donne rien \n{} combinent et donne le génotype".format(count_2_0, count_2_1))
print ("\n\nSi 3 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont les 3 combinaisons possible".format(count_3_0, count_3_1, count_3_2, count_3_3))
print ("\n\nSi 4 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison \n{} ont 2 combinaisons".format(count_4_0, count_4_1, count_4_2))
print ("\n\nSi 5 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 1 combinaison ".format(count_5_0, count_5_1))
print ("\n\nSi 6 haplotypes similaires au géno :\n{} ne donne rien \n{} ont 3 combinaison ".format(count_6_0, count_6_3))



#Sortie txt générale.
with open(first_txt_output,'w') as txt_otp1 :
	txt_otp1.write("Noms des fichiers passés en input : \nPour les haplotypes : {}\nPour les génotypes : {}".format(haplotype, genotype))
	txt_otp1.write("\nNombre d'objet Haplotype créé : {}".format(len(lst_of_haplo_object)))
	txt_otp1.write("\nNombre d'objet Genotype créé : {}".format(len(lst_of_geno_object)))
	txt_otp1.write("\nSéquences composées de {} marqueurs".format(len(lst_of_geno_object[1].markers)))
	txt_otp1.write("\nLes marqueurs des genotypes sont {}:".format(lst_of_geno_object[1].markers))
	txt_otp1.write("\n\nSi 2 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} on une combinaison qui redonne le génotype".format(count_2_0, count_2_1))
	txt_otp1.write("\nSi 3 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} ont 1 combinaison \n{} ont 2 combinaisons \n{} ont les 3 combinaisons possible".format(count_3_0, count_3_1, count_3_2, count_3_3))
	txt_otp1.write("\nSi 4 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} ont 1 combinaison \n{} ont 2 combinaisons".format(count_4_0, count_4_1, count_4_2))
	txt_otp1.write("\nSi 5 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} ont 1 combinaison ".format(count_5_0, count_5_1))
	txt_otp1.write("\nSi 6 haplotypes sont similaires au génotype :\n{} ont 0 combinaisons viables \n{} ont 3 combinaisons ".format(count_6_0, count_6_3))
