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

    """
    #test
    lst_pattern_haplo1 = []
    haplo1 = lst_of_haplo_object[0].sequence
    chain = range(windows_size +1)

    for s in reversed(chain[2:]) :
        print ("#"*10, s, "#"*10)
        for pattern in tw.windows(haplo1, s):
            print (pattern)
            lst_pattern_haplo1.append(pattern)
        print(len(lst_pattern_haplo1))


    lst_test =  lst_of_haplo_object[:5]
    chain = range(windows_size +1)
    #test2 
    for haplo in lst_test :
        for s in reversed(chain[2:]) :
            for pattern in tw.windows(haplo.sequence, s) :
                for other_haplo in lst_test :
                    if tw.KnuthMorrisPratt(other_haplo.sequence, pattern) :
                        print (tw.KnuthMorrisPratt(other_haplo, pattern))
    """


    lst_test =  lst_of_haplo_object[:5]
    #test3
    for haplo in lst_test :
        pattern = tw.windows(haplo.sequence, windows_size)
        for other_haplo in lst_test :
            if tw.KnuthMorrisPratt(other_haplo.sequence, pattern) :
                print (tw.KnuthMorrisPratt(other_haplo, pattern))


"""
    #plus qu'a appeler le fonction comme ça
    chain = range(windows_size +1)
    for haplo in lst_of_haplo_object :
        for s in reversed(chain) :
            print (s)
            for haplox in tw.windows(haplo.sequence, s):
                print (haplox)
                if tw.KnuthMorrisPratt(haplo, haplox):
                    print ("OK")
        print("################")
"""