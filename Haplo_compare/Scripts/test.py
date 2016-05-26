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


    with open(haplotype_c_file, 'r') as my_haploC, open(output, 'w') as my_otp:
        my_haploC_reader = csv.reader(my_haploC, delimiter="\t")
        my_otp_writer = csv.writer(my_otp, delimiter="\t")

        dico_SNP_contigue = {}
        header = True
        

        #parcour du fichier d'alignement ligne par ligne
        for rows in my_haploC_reader :
            #traitement pendant la ligne d'en-tête
            if header :
                #creation du dicotionaire ou je vais ranger chaque portion de SNP contigues (id1, id2, startPos, endPos) commum en fonction de leur longeur (clef)
                marker_size = len(rows[2:-1])
                for x in range(marker_size+1) :
                    #instanciation du dictionnaire par une liste vide.
                    dico_SNP_contigue[x] = []
                header = False
            else :
                #create the future output line
                line = [rows[0], rows[1]]
                #séquence résultat de l'alignement des deux séquences rows[0] et rows[1]
                pattern = rows[2:-1]
                #compteur des SNPs contigues
                contigues = 0
                #compteur de SNP (index)
                count = 0

                #parcour de la séquence pattern SNP par SNP
                for snp_allele in pattern :
                    count +=1

                    #cas du 79ème SNP
                    if count == len(pattern) :
                        if snp_allele == "0" :
                            if contigues == 0 :
                                #create the fuure output line
                                line = [rows[0], rows[1]]
                                line.append(count)
                                line.append(count)
                                contigues += 1
                                dico_SNP_contigue[contigues].append(line)
                            else :
                                contigues += 1
                                line.append(count)
                                dico_SNP_contigue[contigues].append(line)


                    #cas du SNP contigue
                    elif snp_allele == "0" :
                        if contigues == 0 :
                            #create the fuure output line
                            line = [rows[0], rows[1]]
                            line.append(count)
                            contigues += 1
                        else :
                            contigues +=1

                    #cas du SNP non contigue
                    else :
                        line.append(count-1)
                        dico_SNP_contigue[contigues].append(line)
                        contigues = 0
                        #cas particulier de la clef 0 du dico_SNP_contigue. Y sera présent l'index du la endPos seulement



        #écriture du fichier de sortie
        for key, val in dico_SNP_contigue.items() :
            for lst in val :
                my_otp_writer.writerow(lst)
            print(lst)