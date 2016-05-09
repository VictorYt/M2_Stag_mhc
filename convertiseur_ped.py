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
            header.append(rows[1])

    return header


def line_maker(seq):
    """Return a list of allele format we want"""
    geno = []



    return geno

def body_line_maker(ped_f, line):
    """Return the body line to write in my otp"""
    body_line = []

    with open(ped_f, 'r') as my_ped :
        my_ped_reader = csv.reader(my_ped, delimiter="\t")
        count = 0

        for rows in my_ped_reader :
            count+=1
            if count == line :
                rows[1] + line_maker(rows[6:])
                body_line.append(rows[1])




    return body_line



def write_output_file(ped_f, map_f, otp_f):
    """Function that write the output file we want"""
    header_line = header_line_maker(map_f)
    body_line = []


    with open(otp_f, 'w') as my_otp :
        my_otp_writer = csv.writer(my_otp, delimiter="\t")