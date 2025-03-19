# Amino Acid Frequencies:

#Write a program that makes a table of the amino acid frequencies on the ecoli proteome
'''
AA	Frequency	AA	Frequency	AA	Frequency	AA	Frequency	AA Frequency
Ala	0.02		Glu	0.01		Leu	0.09		Ser	0.06
Arg	0.04		Gln	0.05		Lys	0.01		Thr	0.07
Asn	0.03		Gly	0.05		Met	0.03		Trp	0.04
Asp	0.01		His	0.09		Phe	0.05		Tyr	0.09
Cys	0.07		Ile	0.08		Pro	0.08		Val	0.01	

'''

three_letter_code = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys', 
	'E': 'Glu', 'Q': 'Gln', 'G': 'Gly', 'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys', 
    'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser', 'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 
    'V': 'Val'}

import sys
import mcb185


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	total = 0
	amino_acids = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 
	'P', 'S', 'T', 'W', 'Y', 'V']
	count = {}
	for aa in amino_acids:
		count[aa] = 0
	for aa in seq:
		if aa not in count:	count[aa] = 0
		count[aa] += 1
		total += 1
	for aa in count:
		count[aa] /= total

print("AA  Freq	AA  Freq	AA  Freq	AA  Freq")
print("--------------------------------------------------------")
x = 1
for aa, p in count.items():
	if aa in three_letter_code:
		code = three_letter_code[aa]
	else:
		code ='N/A'
	print(f'{code} {100*p:.2f}', end='\t')
	if x % 4 == 0: print()
	x += 1
	
"""

aa_table = list(count.keys())
for i in range(0, len(aa_table), 4):
	for j in range(i, i+4):
		if j < len(aa_table):
			aa, freq = aa_table[j]
			if aa in three_etter_code:
				code = three_letter_code[aa]
			else:
				code = 'N/A'
			print(f"{code:<20} {freq*100}", end="\t")
		print()
	

for aa, freq in count.items():
	count[aa] = freq / total
	aa_table = []
	aa_table.append([three_letter_code[aa], count[aa]])


print("AA\tFrequency\tAA\tFrequency\tAA\tFrequency\tAA\tFrequency")

for i in range(0, len(aa_table), 4):
	rows = [aa_table[i:i+4]






# count the frequencies

frequencies = aa_freq(seq)
aa_table = []
for aa, freq in 

# wanna now make a dictionary with the 20 aa
aa_count = {}
for aa in 'ARNDCEQGHILKMFPSTWYV'
	aa_count[aa] = 0
total_aa_count = 0

# now lets like look for the amino acids in the sequence kinda

for aa, freq in count.items():
	if aa in aa_count:
		aa_count[aa] += freq
		'''
	'''
	for row in rows:
	for aa in row:
		print(aa[0], aa[1], end="\t")
	print()
"""
		