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
 
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Recombinaison finding 0.1')
    print (arguments)


    windows_size = arguments["--windows"]
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

    dirname = output

    try:
        os.makedirs(dirname)
    except OSError:
        if os.path.exists(dirname):
            # We are nearly safe
            pass
        else:
            # There was an error on creation, so make sure we know about it
            raise



    #lecture du fichier
    """Construction of the list of Haplotype object"""
    lst_of_haplo_object = read_input_file(haplotype_file, Haplotype, "\t")


    #plus qu'a appeler le fonction comme ça
    for haplo in lst_of_haplo_object :
        for haplox in windows(haplo.sequence, windows_size):
            print(haplox)
        print("################")