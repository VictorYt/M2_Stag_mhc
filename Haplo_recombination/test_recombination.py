#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


import sys 
import csv


#file = sys.argv[1]


contignous_dico = {}
#lui donnée les clefs?


#distribution du nombre de (mis)match contigues
with open(, 'w') as inpt:
	my_inpt_reader = csv.reader(inpt, delimit="\t")

	for rows in my_inpt_reader:
		contignous_mismatch = 0
		for allele in rows[2:-1]:
			if int(allele) == 1 :
				contignous_mismatch +=1
			else :
				contignous_mismatch = 0
				contignous_dico[len(contignous_mismatch)] = #? index 









#http://stackoverflow.com/questions/18715688/find-common-substring-between-two-strings
#retrouver partie commune
#1
def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer

print longestSubstringFinder("apple pie available", "apple pies")
print longestSubstringFinder("apples", "appleses")
print longestSubstringFinder("bapples", "cappleses")



#2
def common_start(sa, sb):
    """ returns the longest common substring from the beginning of sa and sb """
    def _iter():
        for a, b in zip(sa, sb):
            if a == b:
                yield a
            else:
                return

    return ''.join(_iter())

#3
def stop_iter():
    """An easy way to break out of a generator"""
    raise StopIteration

def common_start(sa, sb):
    ''.join(a if a == b else stop_iter() for a, b in zip(sa, sb))

def terminating(cond):
    """An easy way to break out of a generator"""
    if cond:
        return True
    raise StopIteration

def common_start(sa, sb):
    ''.join(a for a, b in zip(sa, sb) if terminating(a == b))

#4
import itertools as it
''.join(el[0] for el in it.takewhile(lambda t: t[0] == t[1], zip(string1, string2)))



#test
def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
   longest, x_longest = 0, 0
   for x in range(1, 1 + len(s1)):
       for y in range(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > longest:
                   longest = m[x][y]
                   x_longest = x
           else:
               m[x][y] = 0
   return s1[x_longest - longest: x_longest]

#http://codereview.stackexchange.com/questions/21532/python-3-finding-common-patterns-in-pairs-of-strings