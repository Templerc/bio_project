#!/usr/bin/env python3 

import argparse

###--------- funnction to parse command-line arguments 
def get_args():
    ###---------------- accept and parse command line arguments 
    # create an argument parser object
    parser = argparse.ArgumentParser(description="This script calculates the number at a given position in the Fibonacci sequence")

    # Add a positional argument, in this case, the position in the Fibonacci sequence 
    parser.add_argument('fibposition', help="position in the Fibonacci sequence", type=int)

    # an optional argument for verbose output or not
    # if 'store_true', this means assign 'True' if the optional argument is specified 
    # on the command line, so the defualt for 'store_true' is acutally false
    parser.add_argument("-v", "--verbose", help="Print verbose output", action='store_true')

    # parse the arguments and return in two steps
    args = parser.parse_args()
    return args
    # one step 
#    return parser.parse_args()



###--------- function to calculate the fibonacci number
def fib():
    # initialize two integers
    a,b = 0,1

    for i in range(int(args.fibposition)):
        a,b = b,a+b
        fibonacci_number = a 
        return fibonacci_number

###--------- function to print the output
def print_output(output):
    if args.verbose:
        print(f"The Fibonacci number for {args.fibposition} is {output}.")
    else: 
        print(output)



###---------- define the main() function
def main():
    fibnum = fib()
    output = print_output(fibnum)



###---------- calling get_args() happens out here on its own
args = get_args()


# set the environment for this script
# is this main (i.e. a standalone Python script), 
# or is this a Python module being called by another script
if __name__ == '__main__':
    main()