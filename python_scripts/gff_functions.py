#!/usr/bin/env python3

# define function within the module "gff_functions.py" that will be used by the main function in parse_gff 
def read_fasta(fasta_file):
    gseq = ""
    with open(fasta_file, 'r') as f:
        # skip the header line
        next(f)
        # strip each line
        for line in f:
            gseq += line.strip()
    
    return(gseq)

def read_gff(gff_file, gseq):
    features = []

    with open(gff_file, 'r') as g:
        for line in g:
            if line.startswith("#"):
                continue

            cols = line.strip().split("\t")

            start = int(cols[3]) - 1 
            end = int(cols[4])

            # extract sequence
            seq = gseq[start:end]

            # extract ID
            attributes = cols[8]
            seq_id = None

            for item in attributes.split(";"):
                if item.startswith("ID="):
                    seq_id = item.replace("ID=", "")
                    break

            features.append((seq_id, seq))

    return features

###--------- function to print the output
def write_output(features):
    with open("covid_genes.fasta", "w") as out:
        for seq_id, seq in features:
            out.write(f">{seq_id}\n")
            out.write(seq + "\n")