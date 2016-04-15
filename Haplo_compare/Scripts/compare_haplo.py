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


    #############

    """Récupération des instances de Genotype et d'Haplotype_c dans des list"""
    #geno
    lst_geno_obj = read_input_file(genotype_file, Genotype, "\t")
    #haplo (list global)
    lst_k_haplo_obj = read_input_file(known_haplo, Haplotype, "\t")
    lst_c_haplo_obj = read_input_file(candidate_haplo, Haplotype, "\t")
    lst_f_haplo_obj = read_input_file(fastPhase_haplo, Haplotype, "\t")
    #haplo séparé par ori (known/candidate/fP)



    #############

    """Retrouver les haplo similaire entre Known/fP et Candidate/fP"""
    #faire une sortie pour le diagram de venn des haplotye de fP avec les nom de Known et Candidate quand c'est le cas
        #peut être pas besoin si matlib-venn prend les listes des sequences(mais peut être plus long)
    #faire le diagrame de venn avec matlib-venn