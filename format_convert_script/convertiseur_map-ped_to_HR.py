#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (--ped <ped_file>) (--map <map_file>)
    __main__.py (--ped <ped_file>) (--map <map_file>) [-o <filename>]

options:
    -h, --help                              This help.
    -v, --version                           Displays program's version.
    --ped <ped_file>                        Ped input file
    --map <map_file>                        Map input file
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
    map_file = arguments["--map"]
    output = arguments["--output"]
    
    #    {'--help': False,
    #     '--ped_file':ped_file,
    #     '--map_file':map_file,
    #     '--output': "Output_data"

    def header_line_maker(map_f):
        """Return the header line list

        Named parameters :
        map_f -- the map file who will be read

        """
        header = []
        header.append("haplo")

        with open(map_f, 'r') as my_map :
            my_map_reader = csv.reader(my_map, delimiter="\t")

            for rows in my_map_reader :
                header.append(rows[1]) #rows[1] is the SNP name, rows[3] the SNP position

        return header


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
        asso = ['A/C','A/G','A/T','C/G','C/T','G/T']

        for allele in piece(seq,2) :
            A1 = allele[0]
            A2 = allele[1]
            #possible cases
            #missing data
            if A1 == '0' and A2 == '0' :
                geno.append('--')
            #Hmz alleles
            elif A1 == A2 :
                geno.append(A1)
            #Htz alleles
            elif str(A1+"/"+A2) not in asso :
                geno.append(A2+"/"+A1)
            else :
                geno.append(A1+"/"+A2)

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
                sample.append(rows[1])
                sample.extend(line_maker(rows[6:]))
                body_line.append(sample)

        return body_line


    def write_output_file(ped_f, map_f, otp_f):
        """Function that write the output file we want

        Named parameters :
        ped_f -- the ped file taht contain genotype sequences
        map_f -- the map_f that contain markers information (for our header)
        otp_f -- the output name file

        """
        with open(otp_f, 'w') as my_otp :
            my_otp_writer = csv.writer(my_otp, delimiter="\t")

            my_otp_writer.writerow(header_line_maker(map_f))
            for indiv_sample in body_line_maker(ped_f) :
                my_otp_writer.writerow(indiv_sample)






    #__main__
    write_output_file(ped_file, map_file, output)