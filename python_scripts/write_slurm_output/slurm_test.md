#!/bin/bash
#SBATCH --job-name = big_analysis
#SBATCH --partition = comp01
#SBATCH --nodes = 1
#SBATCH --qos comp
#SBATCH --cpus-per-task = 32
#SBATCH --time =  01:00:00
#SBATCH --output = %x.%j.out
#SBATCH --error = %x.%j.err
# #SBATCH --mail-type = ALL
# #SBATCH --mail-user = ctempler@uark.edu


