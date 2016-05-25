#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (--ped <ped_file>)
    __main__.py (--ped <ped_file>) [-o <filename>]

options:
    -h, --help                              This help.
    -v, --version                           Displays program's version.
    --ped <ped_file>                        Ped input file
    -o <filename>, --output <filename>      Specifying output file prefix
                                            [default: Output_data]

"""

if __name__ == "__main__":
    from docopt import docopt
    import os
    import csv
    import itertools as it #used fonction chain & islice
 
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Haplotype rebuilding 0.3')
    print (arguments)

    ped_file = arguments["--ped"]
    output = arguments["--output"]
    
    #    {'--help': False,
    #     '--ped_file':ped_file,
    #     '--output': "Output_data"


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
        dico_multiphasta = {'AC':'M','AG':'R','AT':'W','CG':'S','CT':'Y','GT':'K'}

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


    def body_line_maker(ped_f):
        """Return the body line to write in my otp
        it's a list of line_maker

        Named parameters :
        ped_f -- the ped file to read (contain genotype sequences)

        """
        body_line = []

        with open(ped_f, 'r') as my_ped :
            my_ped_reader = csv.reader(my_ped, delimiter=" ")

            for rows in my_ped_reader :
                sample = []
                sample.append(rows[1]) #rows[1] is the name of the genotype sample
                sample.extend(line_maker(rows[6:]))
                body_line.append(sample)

        return body_line


    def write_output_file(ped_f, otp_f):
        """Function that write the output file we want

        Named parameters :
        ped_f -- the ped file taht contain genotype sequences
        otp_f -- the output name file

        """
        with open(otp_f, 'w') as my_otp :
            for indiv_sample in body_line_maker(ped_f) :
                my_otp.write(">"+indiv_sample[0]+"\n")
                sequence = indiv_sample[1:]
                for values in sequence :
                    my_otp.write(values)
                my_otp.write("\n")







    #__main__
    write_output_file(ped_file, output)