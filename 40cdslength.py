import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:   # will take the file name in the command line
	for line in fp:   # runs through every line in the file
		if line[0] != '#': # skips over the comment lines (first character of the line
						   # cuz why would u need it lol
			words = line.split() # turns the string into a list of words
			if words[2] == 'CDS': # want only the CDS features since this has to do w gene
				beg = int(words[3]) # get the beginning of CDS (coding sequence) but need 
									# as a number/integer to do math
				end = int(words[4]) # get the ending
				print(end - beg + 1) # get the length of the CDS, end-beg, we add 1
									 # gene includes both start and end positions and so
									 # we need to include all positions in the range
									 # ex. 5-3 = 2 but we need to count 2,3,4
									 
									