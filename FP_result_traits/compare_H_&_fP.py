#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#Compare our haplotype versus fastPHASE haplotypes


"""
usage: 
    __main__.py (-m <file>) (-f <file>)
    __main__.py (-m <file>) (-f <file>) [-o <filename>]

options:
    -h, --help                              This help.
    -v, --version                           Displays program's version.
    -m <file>, --mine <file>                Haplotypes input file you known befroe the fastPHASE
    -f <file>, --fPHASE <file>				Haplotypes input file you known from the fastPHASE software
    -o <filename>, --output <filename>      Specifying output file prefix
                                            [default: Compa_data]
"""

if __name__ == "__main__":
	from docopt import docopt
	import csv
	import itertools as it

	# Parse arguments, use file docstring as a parameter definition
	arguments = docopt(__doc__, version='Compare Mine to fPHASE 0.1')
	print (arguments)

	outpt = arguments["--output"]
	mine = arguments["--mine"]
	fPHASE = arguments["--fPHASE"]


	#############################################################################
	#############################################################################	

	class Haplotype(object):
		def __init__(self, name, sequence, markers):
			"""Class constructor Haplotype

			Haplotype Class is characterized by :
				-A name, 
				-a sequence

			"""
			self._name = name 
			self._sequence = sequence
			self._markers = markers

		############
		#ACCESSEURS#
		############

		def _get_name(self):
			"""Return the attribut name of the Haplotype class"""
			return self._name

		def _get_sequence(self):
			"""Return the attribut sequence of the Haplotype class"""
			return self._sequence

		def _get_markers(self):
			"""Return the attribut markers of the Haplotype class which is
			a list of the markers names used for genotyping 
			
			"""
			return self._markers

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

		def _set_markers(self, lstmarkers):
			"""Change the markers list of our Haplotype object by a new one

			Named parameters :
			lstmarkers -- the new markers list selected (here the header of the input)
			
			"""
			self._markers = lstmarkers 

		############
		#PROPERTIES#
		############

		name = property(_get_name, _set_name)
		sequence = property(_get_sequence, _set_sequence)
		markers = property(_get_markers, _set_markers)

	#############################################################################
	#############################################################################




	#creation d'une instance d'haplo fausse pour que la fonction read_file fonctionne (pas bien mais rapide et pas 2 fonctions a faire pour le moment)
	A = Haplotype(name="fake", sequence="fake", markers="fake")

	lst_of_mine_haplo = [A, A]
	lst_of_fP_haplo  = []


	def read_file(filename):
		"""Return a list of object"""
		lst_of_objects = []
		with open(filename, 'r') as src :
			my_reader = csv.reader(src, delimiter="\t")

			if filename == mine :
				header = True
				for rows in my_reader :
					if header : 
						lst_markers = rows[1:]
						header = False
					else :
						A = Haplotype(name=rows[0], sequence=rows[1:], markers=lst_markers)
						lst_of_objects.append(A)
			else :
				SNPs = lst_of_mine_haplo[0].markers #est ce que ça va passer du premier coup? ==> non si lst_of_mine_haplo demare vide
				counter = 0
				for rows in my_reader :
					counter += 1
					fP_name = "fPHASE_haplo_"+str(counter)
					seq = list(rows[0])
					F = Haplotype(name=fP_name, sequence=seq, markers=SNPs)
					lst_of_objects.append(F)

		return lst_of_objects


	lst_of_mine_haplo = read_file(mine)
	lst_of_fP_haplo  = read_file(fPHASE)




	def compare_two_seq(haplo1, haplo2):
		"""Return a list with the name of the 2 Haplotypes objects,
		a sequence with booleen (0, 1) and a int

		0 means no missmatch between the 2 Haplotypes sequence objects for the selected markers 
		1 means that there is a missmatch
		The int at the end of the returned list is the sum of 1 in the sequence 
		(= number of missmatch).

		Named parameters :
		haplo1 -- The fisrt Haplotype object to compare
		haplo2 -- The second Haplotype object to compare

		"""
		output_line = []
		count_erreur = 0
		output_line.append(haplo1.name)
		output_line.append(haplo2.name)
		for i in range(len(haplo1.sequence)) :
			if haplo1.sequence[i] == haplo2.sequence[i] :
				output_line.append(0)
			else :
				output_line.append(1)
				count_erreur += 1
		output_line.append(count_erreur)
		return output_line



	def compare_output(otp, firstobjcetlist, secondobjcetlist):
		"""Return nothing but give the csv output file with the compraison of 
		one sequence between a list of one. 

		Named parameters :
		-otp -- The output name
		-firstobjcetlist -- Can be a list of Genotypes objects or Haplotypes objects
		-secondobjcetlist -- A list of Haplotypes objects

		"""
		with open(otp, 'w') as otp_comparaison :
			my_otp_writer = csv.writer(otp_comparaison, delimiter="\t")

			header =[]
			header.append("Mine_Haplotype")
			header.append("fPHASE_Haplotype")	
			for markers in firstobjcetlist[0].markers :
				header.append(markers)
			header.append("nb_errors")
			my_otp_writer.writerow(header)


			for mhaplo, fhaplo in it.product(firstobjcetlist, secondobjcetlist) :
				my_otp_writer.writerow(compare_two_seq(mhaplo, fhaplo))				


	sortie = outpt+"_details"
	compare_output(sortie, lst_of_mine_haplo, lst_of_fP_haplo)



	def have_same_format(otp, lstoffPhaseHaplo):
		"""Return nothing 
		Give us the fastPHASE haplotype in the same format than the others

		"""
		with open(otp, 'w') as otp_format :
			my_otp_writer = csv.writer(otp_format, delimiter="\t")

			header =[]
			header.append("fastPHASE_name")
			for markers in lstoffPhaseHaplo[0].markers :
				header.append(markers)
			my_otp_writer.writerow(header)

			for fPhaplo in lstoffPhaseHaplo :
				otp_line = []
				otp_line.append(fPhaplo.name)
				for allele in fPhaplo.sequence :
					otp_line.append(allele)
				my_otp_writer.writerow(otp_line)


	sortie2 = "fastPHASE_haplo_same_format"
	have_same_format(sortie2, lst_of_fP_haplo)

	#def compare_list_haplo(listofmine, listoffPhase):
	#	""""""