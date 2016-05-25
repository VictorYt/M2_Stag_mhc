#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (--ih <haplo_file>) (-w <size>)
    __main__.py (--ih <haplo_file>) (-w <size>) [-o <filename>] [-t <nb>]

options:
    -h, --help                              This help.
    -v, --version                           Displays program's version.
    --ih <haplo_file>                       Haplotype input file
    -w <size>, --windows <size>				Windows size
    -o <filename>, --output <filename>      Specifying output file prefix
                                            [default: Output_recom_data]
    -t <nb>, --threshold <nb>               Threshold of accepted errors during the comparing windows step
                                            [default: 0]


"""

if __name__ == "__main__":
    from docopt import docopt
    import time
    #from Object import ClassName, function ...
    from HaplotypeR import Haplotype
    import test_windows as tw
 
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Recombinaison finding 0.1')
    print (arguments)


    windows_size = int(arguments["--windows"])
    output = arguments["--output"]
    threshold = arguments["--threshold"]
    haplotype_file = arguments["--ih"]



    
    #    {'--help': False,
    #     '--input_haplotype':file,
    #     '--windiws':size,
    #     '--output': "Output_data",
    #     '--threshold': 0,
    #     '--version': False}


    #http://sametmax.com/path-py-plus-en-detail/

#pendant le script:
    #sequence de la fenêtre
    #chez qu'elle autre haplotype elle est retrouvé



    #lecture du fichier
    """Construction of the list of Haplotype object"""
    lst_of_haplo_object = tw.read_input_file(haplotype_file, Haplotype, "\t")
    

    lst_test =  lst_of_haplo_object[:5]
    #test3
    for haplo in lst_test :
        print (haplo.sequence)
        pattern = tw.windows(haplo.sequence, windows_size)
        for other_haplo in lst_test :
            for p in pattern :
                print ("#"*10)
                for index in tw.KnuthMorrisPratt(other_haplo.sequence, p) :
                    print(index)
    #PAS BON IL FAUT QUE JE GARDE LES MÊME INDEX DE FENÊTRE A CHAQUE FOIS (BIEN CAR PLUS DE RECHERCHE MAIS JUSTE DE LA COMPARAISON D'ALIGNEMENT)



