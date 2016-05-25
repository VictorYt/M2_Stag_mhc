#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (-i <geno_file>) [-o <fasta_filename>]

options:
    -h, --help                                              This help.
    -v, --version                                           Displays program's version.
    -i <geno_file>, --input <geno_file>                     Haplotype input filenmane
    -o <fasta_filename>, --output <fasta_filename>          Output Name
                                                            [default: Fasta_data]

"""

if __name__ == "__main__":
    from docopt import docopt
    import csv
    
    arguments = docopt(__doc__, version='HR_to_fasta_file 0.2')
    print (arguments)

    genotype_file = arguments["--input"]
    fasta = arguments["--output"]+".fas" #A fisrt one for the homozygous genotype

    #    {'--help': False,
    #     '--input_haplotype': geno_file,
    #     '--output': fasta_filename,
    #     '--version': False}



    def line_maker(seq):
        """Return a list of allele format we want

        Named parameters :
        seq -- the sequence that i want to change the format

        """
        geno = []
        #asso = ['AC','AG','AT','CG','CT','GT']
        dico_multiphasta = {'A/C':'M','A/G':'R','A/T':'W','C/G':'S','C/T':'Y','G/T':'K'}

        for allele in seq :
            #possible cases
            #missing data
            if allele == '--' :
                geno.append("?")
            #Hmz alleles
            elif len(allele) == 1 :
                geno.append(allele)
            #Htz alleles
            else :
                geno.append(dico_multiphasta[str(allele)])

        return geno




    with open(genotype_file, 'r') as geno_src , open(fasta, 'w') as fasta_output:
        my_geno_reader = csv.reader(geno_src, delimiter="\t")
        
        header = True
        for rows in my_geno_reader :
            if header :
                header = False
            else :
                fasta_output.write(">"+rows[0]+"\n")
                sequence = rows[1:]
                for values in line_maker(sequence) :
                    fasta_output.write(values)
                fasta_output.write("\n")