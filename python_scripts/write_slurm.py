#!/usr/bin/env python3

job_name = '__________'
wall_time = '__________'
queue_name = '__________'
notification = '__________'

print('#!/bin/bash')
print(f'#SBATCH --job-name={job_name}')
print(f'#SBATCH --partition {queue_name}')
print('#SBATCH --nodes=1')
print('#SBATCH --qos comp')
print('#SBATCH --cpus-per-task=32')
print(f'#SBATCH --time={wall_time}')
print('#SBATCH --output=%x.%j.out')
print('#SBATCH --error=%x.%j.err')
print('# #SBATCH --mail-type=ALL')
print(f'# #SBATCH --mail-user={notification}')

#copy files

#cd into where the files are (on scratch)
print('cd /') 
#commands
