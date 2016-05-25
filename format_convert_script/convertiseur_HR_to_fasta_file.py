#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (-i <geno_file>) [-o <fasta_filename>]

options:
    -h, --help                              				This help.
    -v, --version                           				Displays program's version.
    -i <geno_file>, --input <geno_file>                     Haplotype input filenmane
    -o <fasta_filename>, --output <fasta_filename>      	Output Name
                                            				[default: Fasta_data]

"""

if __name__ == "__main__":
    from docopt import docopt
    import csv
    
    arguments = docopt(__doc__, version='Tab_to_fasta_file 0.2')
    print (arguments)

    genotypefile = arguments["--input"]
    fasta = arguments["--output"]+".fas" #A fisrt one for the homozygous genotype

    #    {'--help': False,
    #     '--input_haplotype': geno_file,
    #     '--output': fasta_filename,
    #     '--version': False}

    def function():
        pass



#1) Lire le fichier tabule
    with open(genotypefile, 'r') as geno_src , open(fasta, 'w') as fasta_output:
        my_geno_reader = csv.reader(geno_src, delimiter="\t")
        
        header = True
        for rows in my_geno_reader :
            if header :
                header = False
            else :
                fasta_output.write(">"+rows[0]+"\n")
                sequence = rows[1:]
                for values in sequence :
                    fasta_output.write(values)
                fasta_output.write("\n")