
'''
SET: a mutable container and all elements are unique/unordered
------------------------------------------------------------------------------------------
'''

s = {'A', 'C', 'G'}
print(s)

'''
when print, the order will always change
'''

s.add('T')
print(s)

# adding the same element doesn't do anything 
'''
ex) s.add('A')
	print(s)
'''

# calling for an index in the set will result in an error, since no order
'''
ex) print(s[2])
'''

# As data grows, set-based lookups become exponentially faster than list-based ones

'''
DICTIONARIES: indices are strings instead of numbers
-----------------------------------------------------------------------------------------
'''

# indices are strings instead of numbers
'''
ex) list[0] - 0 is a numeric index
	dict['hey'] - 'hey' is a string index
'''	

# no append() for dictionaires, each item in a dictionary is key:value pair
# 		- the key is string in square brackets
#		- the value is anything put in a variable

# to create an empty dictionary
d = {}
d = dict()

#to make dictionary with predefined items -- use curly brack and key:value pair
d = {'dog': 'woof', 'cat': 'meow'}
print(d)

# To access items use square brackets.
print(d['cat'])

# To add new items to a dictionary, assign a new key:value pair.
d['pig'] = 'oink'
print(d)

# To change the value of an item, access it with its key.
d['cat'] = 'mew'
print(d)

# To delete an item, use del.
del d['cat']
print(d)

# If you try to access a key that doesn't exist, you get an error.
print(d['rat'])

# To check if a key exists, use the keyword in just as you would with a list or a set.
if 'dog' in d: print(d['dog'])

'''
ITERATIONS IN DICTIONARY
'''

# the standard for oops iterates over keys in order of creating
for key in d: print(f'{key} says {d[key]}')

# iterate with dict.items()
for k, v in d.items(): print(k, 'says' v)
# unpack the tuples, do not keep it like below
for thing in d.items(): print(thing[0], thing[1])

# print just the keys, values as returned iterable objects
# print as an actual list , coerce w list
print(d.keys(), d.values(), list(d.values()))

'''
TABLES
'''
kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
    
    
'''
IF WANT TO COUNT COMPOSITION OF LETTERS
'''
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1

'''
SORTING
------------------------------------------------------------------------------------------
'''

'''Command Line Methods'''
'''
python3 51countgff.py ecoli.gff.gz | sort
---- sorts output by feature name

python3 51countgff.py ecoli.gff.gz | sort -n -k 2
---- sorts second column (-k 2) numerically (-n)

python3 51countgff.py ecoli.gff.gz | sort -nk2
---- merged together

** k must be after n since has an argument
'''

# Sorting by keys (sorted function)
for k in sorted(count): print(k, count[k])

# sorted function needs a list of things to sort, which is keys

# Sort based off values
for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)
# lambda is basically substituting a named function

'''
Determine which kmer is missing
'''
import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)
	
'''
ARGPARSE: python has a functional usage statement in argparse library
------------------------------------------------------------------------------------------
'''

# unix programs have CLI to give usage statement
# a usage statement gives brief explanation on how to use command
#			- what command does, what options and arguments it takes
# 			head --help

