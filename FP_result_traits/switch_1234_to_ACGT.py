#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (-i <file>) (-s <nb>)
    __main__.py (-i <file>) (-s <nb>) [-o <filename>]

options:
    -h, --help                              This help.
    -v, --version                           Displays program's version.
    -i <file>, --input <file>               Haplotype input file
    -o <filename>, --output <filename>      Specifying output file prefix
                                            [default: Switch_data]
    -s <nb>, --skip <nb>                    Number of line you want skip
"""

if __name__ == "__main__":
    from docopt import docopt
    import csv
    import itertools as it

    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Switch 1234 to ACGT 0.1')
    print (arguments)

    outpt = arguments["--output"]
    inpt = arguments["--input"]
    nb_header = arguments["--skip"]

    def switch_nb_to_nt(input, output, header_line):
        """Return nothing but give the file switched without our header (lines skiped)"""
        with open(input, 'r') as src, open(output, 'w') as otp :
            my_reader = csv.reader(src, delimiter="\t")
            my_writer = csv.writer(otp, delimiter="\t")

            for rows in it.islice(my_reader, header_line, None) :
                seq = rows[0]
                seq = seq.replace("1", "A")
                seq = seq.replace("2", "C")
                seq = seq.replace("3", "G")
                seq = seq.replace("4", "T")
                line = [seq, rows[1], rows[2]]
                my_writer.writerow(line)

    switch_nb_to_nt(inpt, outpt, nb_header)