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
            id1 = rows[0]
            id2 = rows[1]

            #traitement pendant la ligne d'en-tête
            if header :
                #creation du dicotionaire ou je vais ranger chaque portion de SNP contigues (id1, id2, startPos, endPos) commum en fonction de leur longeur (clef)
                for windows_size in range(len(rows[2:-1]) +1) :
                    #instanciation du dictionnaire par une liste vide.
                    dico_SNP_contigue[windows_size] = []
                header = False
            
            else :
                #séquence résultat de l'alignement des deux séquences rows[0] et rows[1]
                pattern = rows[2:-1]
                #compteurs et index
                count = 0
                startPos = 0
                endPos = 0
                contig_0 = 0
                contig_1 = 0
                line = []
                

                #parcour de la séquence pattern SNP par SNP
                for snp_allele in pattern :
                    count +=1


                    #cas du premier marqueur
                    if count == 1 :
                        if snp_allele == "1":
                            contig_1 += 1
                        else :
                            contig_0 += 1
                            startPos = count
                            line.append(id1)
                            line.append(id2)
                            line.append(startPos)

                    #cas des marqueur entre le second et l'avant dernier
                    elif count >1 and count < len(pattern) :
                        if snp_allele == "0" and contig_0 > 0 :
                            contig_0 += 1
                        elif snp_allele == "0" and contig_0 == 0 :
                            contig_1 = 0
                            contig_0 += 1
                            startPos = count
                            line.append(id1)
                            line.append(id2)
                            line.append(startPos)
                        elif snp_allele == "1" and contig_1 > 0 :
                            contig_1 += 1
                        else : #si snp_allele == "1" and contig_1 == 0 
                            contig_1 += 1
                            endPos = count - 1
                            line.append(endPos)
                            dico_SNP_contigue[contig_0].append(line)
                            contig_0 = 0
                            line = []

                    #cas du dernier marqueur
                    else : #count == len(pattern)
                        if snp_allele == "0" and contig_0 > 0 :
                            contig_0 +=1 
                            endPos = count #ou len(pattern)
                            line.append(endPos)
                            dico_SNP_contigue[contig_0].append(line)
                        elif snp_allele == "1"and contig_1 == 0 :
                            endPos = count - 1
                            line.append(endPos)
                            dico_SNP_contigue[contig_0].append(line)
                        else :
                            contig_0 += 1
                            startPos = endPos = count
                            line.append(id1)
                            line.append(id2)
                            line.append(startPos)
                            line.append(endPos)
                            dico_SNP_contigue[contig_0].append(line)



        #écriture du fichier de sortie
        head_output = ["id1","id2", "start", "end"]
        my_otp_writer.writerow(head_output)
        for key, val in dico_SNP_contigue.items() :
            for lst in val :
                my_otp_writer.writerow(lst)