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
        """Return the header line list (empty first value and markers list)"""
        header = []
        header.append("")

        with open(map_f, 'r') as my_map :
            my_map_reader = csv.reader(my_map, delimiter="\t")

            for rows in my_map_reader :
                header.append(rows[1]) #rows[1] is the SNP name, rows[3] if we want SNP position

        return header


    def piece(iterable, size, format=tuple):
        """Sliding window of variable size"""
        my_it = iter(iterable)
        while True :
            yield format(it.chain((next(my_it),), it.islice(my_it,size -1)))


    def line_maker(seq):
        """Return a list of allele format we want"""
        geno = []
        asso = ['AC','AG','AT','CG','CT','GT']

        for allele in piece(seq,2) :
            A1 = allele[0]
            A2 = allele[1]
            #possible cases
            #missing data
            if A1 == '0' and A2 == '0' :
                geno.append('--')
            #Hmz alleles
            elif A1 == A2 :
                geno.append(A1*2)
            #Htz alleles
            elif str(A1+A2) not in asso :
                geno.append(A2+A1)
            else :
                geno.append(A1+A2)

        return geno


    def body_line_maker(ped_f):
        """Return the body line to write in my otp"""
        body_line = []

        with open(ped_f, 'r') as my_ped :
            my_ped_reader = csv.reader(my_ped, delimiter=" ")

            for rows in my_ped_reader :
                indiv = []
                indiv.append(rows[1])
                indiv.extend(line_maker(rows[6:]))
                body_line.append(indiv)

        return body_line



    def write_output_file(ped_f, map_f, otp_f):
        """Function that write the output file we want"""
        with open(otp_f, 'w') as my_otp :
            my_otp_writer = csv.writer(my_otp, delimiter="\t")

            my_otp_writer.writerow(header_line_maker(map_f))
            for indiv in body_line_maker(ped_f) :
                my_otp_writer.writerow(indiv)






    #__main__
    write_output_file(ped_file, map_file, output)
