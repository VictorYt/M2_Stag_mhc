#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (-i <haplo_c_file>) 
    __main__.py (-i <haplo_c_file>) [-o <filename>] [-t <nb>]

options:
    -h, --help                                      This help.
    -v, --version                                   Displays program's version.
    -i <haplo_c_file>, --input <haplo_c_file>       Haplotype input file
    -o <filename>, --output <filename>              Specifying output file prefix
                                                    [default: Output_data]
    -t <nb>, --threshold <nb>                       Threshold of accepted errors during haplotype and genotype comparaison 
                                                    [default: 0]

"""

if __name__ == "__main__":
    from docopt import docopt
    import os
    import time
    import csv
    import itertools as it

 
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Haplotype rebuilding 0.3')
    print (arguments)

    haplotype_c_file = arguments["--input"]
    output = arguments["--output"]
    threshold = arguments["--threshold"]


    with open(haplotype_c_file, 'r') as my_haploC :
        my_haploC_reader = csv.reader(my_haploC, delimiter="\t")

        dico_SNP_contigue = {}
        header = True

        for rows in my_haploC_reader :
            if header :
                #creation du dicotionaire ou je vais compter le nombre de fenêtre contigues
                marker_size = len(rows[2:-1])
                for x in range(marker_size+1) :
                    dico_SNP_contigue[x] = 0
                header = False
            else :
                pattern = rows[2:-1]
                for match in pattern :
                    if match == 0 :
                        

                #remplir les valeur du dico now

    pattern = list(pattern) #attention je lui donnerai dejà une liste

    #build table of shift amounts
    shifts = [1] * (len(pattern) +1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    #do the actual search
    startPos = 0
    matchLen = 0
    for c in text :
        while matchLen == len(pattern) or matchLen >= 0 and pattern[matchLen] != c :
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern) :
            yield (startPos)