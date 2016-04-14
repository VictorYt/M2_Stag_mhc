#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (--ik <haplo_file>) (--ic <haplo_file>) (--ip <haplo_file>) (--ig <geno_file>)
    __main__.py (--ih <haplo_file>) (--ic <haplo_file>) (--ip <haplo_file>) (--ig <geno_file>) [-o <filename>]

options:
    -h, --help                              This help.
    -v, --version                           Displays program's version.
    --ik <haplo_file>                       Known haplotype input file
    --ic <haplo_file>                       Candidate haplotype input file
    --ip <haplo_file>                       fastPHASE haplotype input file
    --ig <geno_file>                        Genotype input file
    -o <filename>, --output <filename>      Specifying output file prefix
                                            [default: Output_data]

"""

if __name__ == "__main__":
    from docopt import docopt
    import os
    import time
    import itertools as it
    #from Object import ClassName, function ...
    from Haplotype_c import Haplotype_c
    from Genotype_c import Genotype_c
 
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Haplotype compare 0.1')
    print (arguments)

    output = arguments["--output"]
    known_haplo = arguments["--ik"]
    candidate_haplo = arguments["--ic"]
    fastPhase_haplo = arguments["--ip"]
    genotype_file = arguments["--ig"]

    #http://sametmax.com/path-py-plus-en-detail/