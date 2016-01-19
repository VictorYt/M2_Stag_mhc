#!/usr/bin/env python

dico ={'1':"ACGTACGT",'2':"TAGCTTCAGCAGCT",'3':"CGAGCACACTACTAGACT"}

def getSeqFlanq5():
	for value in dicoSNP.iteritems():
		seqG = list(value[0:99])
	return seqG


print "la sequence en 5' de la key :", dico.keys(),"est :",dico.getSeqFlanq5()