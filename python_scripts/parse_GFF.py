#!/usr/bin/env python3

# use argparse() to accept FASTA genome name and GFF file name
import argparse
import gff_functions

###--------- funnction to parse command-line arguments 
def gff_args():
    ###---------------- accept and parse command line arguments 
    # create an argument parser object
    parser = argparse.ArgumentParser(description="This script will accept the file names for FASTA genome and GFF data")

    # Add a positional argument, in this case, the position in the Fibonacci sequence 
    parser.add_argument('FASTA', help="FASTA genome file name", type =str)

    parser.add_argument('GFF', help="GFF file name", type = str)

    args = parser.parse_args()
    return args

###---------- define the main() function
def main():
    # Read genome sequence
    gseq = gff_functions.read_fasta(args.FASTA)

    # Parse GFF and extract sequences
    features = gff_functions.read_gff(args.GFF, gseq)

    # Write output
    # gff_functions.write_output(features)

###---------- calling get_args() happens out here on its own
args = gff_args()


if __name__ == '__main__':
    main()