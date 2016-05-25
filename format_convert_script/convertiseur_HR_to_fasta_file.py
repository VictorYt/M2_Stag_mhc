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

    def piece(iterable, size, format=tuple):
        """Sliding window of variable size

        Named parameters :
        iterable -- the sequence that i want to cut in piece of 2 alleles
        size -- size of the iterable that we want (here 2)

        """
        my_it = iter(iterable)
        while True :
            yield format(it.chain((next(my_it),), it.islice(my_it,size -1)))

    def line_maker(seq):
        """Return a list of allele format we want

        Named parameters :
        seq -- the sequence that i want to change the format

        """
        geno = []
        #asso = ['AC','AG','AT','CG','CT','GT']
        dico_multiphasta = {'A/C':'M','A/G':'R','A/T':'W','C/G':'S','C/T':'Y','G/T':'K'}

        for allele in piece(seq,2) :
            A1 = allele[0]
            A2 = allele[1]
            #possible cases
            #missing data
            if A1 == '0' and A2 == '0' :
                geno.append("?")
            #Hmz alleles
            elif A1 == A2 :
                geno.append(A1)
            #Htz alleles
            #elif dico_multiphasta.has_key(str(A1+A2)) :
            elif str(A1+A2) not in dico_multiphasta.keys() :
                allele = str(A2+A1)
                geno.append(dico_multiphasta[allele])
            else :
                allele = str(A1+A2)
                geno.append(dico_multiphasta[allele])

        return geno



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