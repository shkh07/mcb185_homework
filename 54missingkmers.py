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

