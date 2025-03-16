import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):  
# for loop gets the next records from teh fasta line and each records is returned as tuple
			# with a definition and sequence
# defline: definition line (> + identifier and description)
# seq --> is the entire sequence as a single string (without line breaks)
# the mcb...fasta tells to read the fasta file
	print(defline[:30], seq[:40], len(seq))
# print the first few characters and the sequence length
# defline[:30] shows the first 30 characters of the definition line
# seq[:40] shows the first 40 bases/amino acids
# len(seq) shows the total sequence length
	
	
	
'''
run it like:
python3 41fasta.py ../MCB185/data/A.thaliana.fa.gz
python3 41fasta.py ../MCB185/data/C.elegans.fa.gz
python3 41fasta.py ../MCB185/data/D.melanogaster.fa.gz
'''