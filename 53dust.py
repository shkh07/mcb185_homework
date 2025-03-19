import argparse

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('-l', '--lower', action='store_true',
	help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)


'''
python3 53dust.py ecoli.fa.gz -l -s 15 -e 2.5
'''

'''
OUTPUT:
dusting with ecoli.fa.gz 15 2.5 True
'''





"""

# argparse is a library that makes it easy to handle command-line arguments

import argparse

parser = argparse.ArgumentParser(description='DNA entropy filter.')
# creates the argument parser object in a variable called parser
# description is the text that will appear when type -h or --help

parser.add_argument('file', type=str, help='name of fasta file')
# adds positional argument for a path to a FASTA file

parser.add_argument('size', type=int, help='window size')
# adds positional argument for window size and specifies it is integer

parser.add_argument('entropy', type=float, help='entropy threshold')
# adds positional argument for entropy threshold which is a float

arg = parser.parse_args()
# creates t arg object from getting values on command line and assigning to various prop
#		ex) arg.file contains path to FASTA file
#		ex) arg.size is window size
#		ex) arg.entropy is entropy threshold

print('dusting with', arg.file, arg.size, arg.entropy)
# gives something to print when we give program the proper number and arguments

'''
OUTPUT:

usage: 53dust.py [-h] file size entropy
53dust.py: error: the following arguments are required: file, size, entropy

---- the -h stands for help and usage statement provides more detail, including final
	 line (tells to also get message with --help = longer version)
	 ** so just put -h after command line arguments
'''

'''
NAMED ARGUMENTS: the arguments are optional and can occur in any order
------------------------------------------------------------------------------------------
'''
import argparse
# sim to sep= or end=''

print('first', 'second')                       # positional only
print('first', 'second', sep='\t', end='\n')   # named
print('first', 'second', end='\n', sep='\t')   # named, different order

# Change size and entropy to be named parameters
'''size is now --size with default=20. Similarly. entropy is now --entropy and default=1.4. 
inside the program, they are accessed exactly as before'''
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)

'''
python3 53dust.py
python3 53dust.py e.coli.fa.gz
python3 53dust.py e.coli.fa.gz --size 15 --entropy 1.2
'''

'''
FLAGS: turns off/on some behavior, program can soft-mask sequences
------------------------------------------------------------------------------------------
'''
import argparse
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

'''
python3 53dust.py e.coli.fa.gz
python3 53dust.py coli.fa.gz --lower
'''

'''
SHORT AND LONG
'''
# --size can be -s and --entropy can be -e
parser.add_argument('-s', '--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
    
"""