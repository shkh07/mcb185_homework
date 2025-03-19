import sys
import mcb185
import itertools
import sequence

no_kmer = True
k = 1

while no_kmer:
	kcount = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		revseq = sequence.revcomp(seq)
		for i in range(len(seq) - k + 1):
			kmer_for = seq[i:i+k]
			kmer_back = revseq[i:i+k]
			if kmer_for not in kcount: kcount[kmer_for] = 0
			if kmer_back not in kcount: kcount[kmer_back] = 0
			kcount[kmer_for] += 1
			kcount[kmer_back] += 1
			
	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts) 
		if kmer not in kcount:
			print(kmer)
			no_kmer = False
	
	k += 1
	
'''
python3 54missingkmers.py ecoli.fa.gz 8 | sort -nk2
python3 54missingkmers.py ecoli.fa.gz 8 | sort -nk2 | wc -l
'''


'''
-----------------------------------------------------------------------------------------


no_kmer = True 
---- flag controls the loop and indicates whether a missing k-mer has been found or not

k = 1
--- starts by looking for missing 1-mers (single nucleotide sequences)

while no_kmer:
---- while loop will continue running till no_kmer is true. it will stop when found

	kcount = {}
---- dictionary to store the count of each observed kmer
---- K is the kmer itself, V is count of how many times kmer appears in sequence

		for i in range(len(seq) - k + 1):
---- loop iterats through positions in DNA sequence to extract all possible k-mers (subseq)
	 of length k --> kmer of length k from both forward/reverse strands
	 
			kmerf = seq[i:i+k]
---- kmerf is kmer from forward strand

			kmerb = revseq[i:i+k]
---- kmerb is kmer from reverse strand

			if kmerf not in kcount: kcount[kmerf] = 0
			if kmerb not in kcount: kcount[kmerb] = 0
---- if either kmer is not yet in kcount, it initializes it with a count of 0

			kcount[kmerf] += 1
			kcount[kmerb] += 1
---- then it increments the count both kmers (both reverse/forward) by 1
			
	for nts in itertools.product('ACGT', repeat=k):
---- loop generates all possible kmers of legnth k from nucleotide basees using itertools
---- repeat=k argument makes sure generate kmers of correct length

		kmer = ''.join(nts) 
---- convert tuple of nucleotides into a string to represent a kmer

		if kmer not in kcount:
---- for each kmer, program checks if it exists in kcount. if no exist, it is missing
			
			print(kmer)
			no_kmer = False
---- print the missing kmer and set to false to stop the loop. this ends search of missing
	 kmers for current k
	
	k += 1
---- if no missing kmer found, program increases k by 1 and loop repeats to search kmer
	 of size k+1
'''