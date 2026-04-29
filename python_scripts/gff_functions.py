#!/usr/bin/env python3

import csv

# define function within the module "gff_functions.py" that will be used by the main function in parse_gff 
def read_fasta(fasta_file):
    gseq = ""
    with open(fasta_file, 'r') as f:
        # skip the header line
        next(f)
        # strip each line
        for line in f:
            gseq += line.rstrip()
    
    return(gseq)

def read_gff(gff_file, seq):
    with open(gff_file, 'r') as g:
    # create a csv reader object
        reader = csv.reader(g, delimiter='\t')
    
    # read file line by line
    for line in reader:
        start = int(line[3]) - 1
        end = line[4] # don't change end due to list slicing needing j+1 in [i, j]
        feature_seq = seq[start:end]
        
        # all this to get the gene name
        attrb = line[8] 
        # split attributes by semicolon 
        attrb_list = attrb.split(";")
        # split the first field on the '=' sign, then the gene name is at the end of the list
        a = attrb_list[0].split('=')
        gene_name = a[-1]
        
        # easy way goes against assignemnt 
        write_output(gene_name, feature_seq)

        # alternatively, store in dictionary, where key = gene_name, value = feature_seq

###--------- function to print the output
def write_output(name, seq):
    print(f">{name}")
    print(seq)