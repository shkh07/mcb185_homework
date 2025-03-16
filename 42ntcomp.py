

"""
GETTING THE COMPOSITIONS-----------------------------------------------------------------
"""

'''
GET THE GC COMPOSITION FROM A SEQUENCE
'''

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split() #splits the defline into words
	name = defwords[0] #uses the first word as the sequence name
	gc = 0 #sets a counter to keep track of how many there are in the sequence
	for nt in seq: # goes thru each nucleotide in the sequence
		if nt == 'C' or nt == 'G': gc +=1  # checks if the nuc is C/G and if yes will
										   # increase the count by one
	print(name, gc/len(seq)) # calculates teh fraction of the sequence that is C/G 
							 # prints the sequence name and its GC composition
							 
							 
'''
COUNT ALL NUCLEOTIDES THRU CREATING INDIVIDUAL VARIABLES
- WILL STACK IF/ELIF/ELSE STATEMETNS TO ASSIGN INDIVIDUALLY
'''
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split() #splits the defline into words
	name = defwords[0] #uses the first word as the sequence name
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0 
	for nt in seq:
		if nt == 'A': A +=1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else: N += 1
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))


'''
WANT TO CREATE A LIST TO HOLD THE COUNTS
 - INSTEAD OF ASSIGNING VARIABLES, USE LISTS AND ASSIGNMENTS AT SPECIFIC INDICES OF LIST 
   VARIABLE CORRESPONDING TO NT
'''

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split() #splits the defline into words
	name = defwords[0] #uses the first word as the sequence name
	counts = [0, 0, 0, 0, 0]  # creates a list with 5 zeroes to represent the nt
	for nt in seq: # for each nt in the sequence
		if nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else: counts[4] += 1
	print(name, end=' ') # prints the name followed by a space and doesnt add a new line
	for n in counts: print(n/len(seq), end=' ') # for n in counts goes through each count 
												# in the list.
												# the print... prints the fraction of each
												# nt
	print() # prints a newline to finish the output the line
	
	
'''
USE INDEXING WITH str.find()
'''
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN' # nts is string containing the nts we're interested in
	counts = [0] * len(nts) # creates a list with the same length as nts, each element is
							# initially 0 and each index corresponds to a nt in nts
	for nt in seq: # for each nt in seq
		idx = nts.find(nt) # searches for nt in the string nts
						   # if it is found, it will return index where located in nts
						   # if not found, it will return -1
						   			# since it is -1, it will be N
		counts[idx] += 1 # increments the count for the nucleotide based on the index
						 # position in nts and counted for
	print(name, end=' ')
	for n in counts: # for each count in the list
		print(n/len(seq), end=' ') # each fraction will be printed on teh same line
								   # we have the fraction of the nt from the whole seq
	print()


'''
IF WANT TO COUNT ALL LETTERS, NEED A MUTABLE CONTAINER = LIST
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = [] # create an empty list to store each unique nucleotide that we lowk see
	counts = [] # create an empty list that will store the count for each nt
	for nt in seq: # for each nt in the seq
		if nt not in nts: # if the nt we find isnt already in the nts list, then bruh add
			nts.append(nt)  # adds the nt in nts
			counts.append(0) # adds a 0 to the counts (to initialize the count for the nt)
		idx = nts.index(nt) # find the index to determine the position in the nts list
		counts[idx] += 1 # increase the count by 1
	print(name) # print the sequence name
	for nt, n in zip(nts, counts): # loop over paired elements from the lists nts and 
								   # counts using the zip()
		print(nt, n, n/len(seq)) # for each nt and its count, print the nucleotide and
								 # its raw count from the list and the fraction
	print()



'''
USING str.count TO COUNT SPECIFIC LETTERS FROM ALPHABET, NEED TO DETERMINE THE ALPHABET
BEFORE THO
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	print(name, end=' ') # print the sequence name on the same line
	for nt in 'ACGTN': # iterates over each character in the string
		print(seq.count(nt) / len(seq), end=' ') # for each nt
												 # seq.count(nt) counts how many times nt
												 			# appears in seq
												 # divides this count by sequence length
												 # print fraction keeping all in one line

"""
END--------------------------------------------------------------------------------------
"""


'''
Another way to count letters is with a dictionary
'''
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1