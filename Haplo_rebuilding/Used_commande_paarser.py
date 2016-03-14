#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py [--ih <haplo_file>] [--ig <geno_file>] ( -o <filename> | -t | -d | -pca)

options:
    -h, --help                       This help.
    -v, --version                    Displays program's version.
    --ih=haplo_file                  Here the haplotype input file
    --ig=geno_file                   Here the genotype input file
    -o <filename>, --output=name     Output Name
                                      [default: "Output_data"]
    -t, --threshold                  Threshold of accepted errors during haplotype and genotype comparaison 
                                      [default: 0]
    -d, --dist                       Produce distribution graphics based on inputs and outputs files. 
                                      [default: False]
    -p, --ACP                        Produce pca graphics based on inputs and outputs files.
                                      [default: False]

"""

if __name__ == "__main__":
    from docopt import docopt
 
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Haplotype rebuilding 0.1')
    print (arguments)

    distribution = arguments["--dist"]
    pca = arguments["--ACP"]
    output = arguments["--output"]
    threshold = arguments["--threshold"]
    haplotype_file = arguments["--ih"]
    genootype_file = arguments["--ig"]

    
    #    {'--help': False,
    #     '--input_haplotype':file,
    #     '--input_genotype':file,
    #     '--output': "Output_data",
    #     '--threshold': 0,
    #     '--dist': False,
    #     '--pca': False,
    #     '--version': False}


    #Est-ce que je doit spécifier ici toutes les possibilité
        #Juste -ih et -ig (obligatoire)
        #Toutes les autres combinaisons 


    if (output == True):
        print ("-o utilisé")#I take the string give by the user and i use it for create all i need
    else :
        print("-o non utilisé")
        output = "HR_output"
        #HR for Haplotype Rebuilding

    # Look at threshold argument
    if (threshold == True):
        print ("-t utilisé")
        print (arguments["-t"])
        #blabla 
    else :
        print ("-t non utilisé")
        arguments["-t"] = 0

    # Look at distribution argument
    if (distribution == True):
        print ("-dist utilisé")
        #Look if the directory "-o filename_distribution" exist
            #if True go in and do distribution graphiques
            #if not create it and go in and do distribution graphiques
            #when it's done go back in the previous directory

        #ou ne pas bouger et les écrires dans le chemin ./"-o filename_distribution" ---> mieux

    # Look at pca argument
    if (pca == True):
        print ("-pca utilisé")
        #idem 

    if (haplotype_file == True):
        print (arguments["<file>"][0])