'''
K-MERS: a sequence of length k, where k is a small integer.
- subsequences of sliding window algorithsm are k-mers. individual nt are kmer of k=1
'''

import sys
import mcb185

k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
for kmer, n in kcount.items(): print(kmer, n) 

'''
python3 52kmercount.py ecoli.fa.gz 1
python3 52kmercount.py ecoli.fa.gz 7 | wc
'''

# Want to determine which kmer is missing for larger k values
import itertools
for nts in itertools.product('ACGT', repeat=k):
	kmer = ''.join(nts)  		# joins tuple nts intro string so we can index to dict
	if kmer in kcount: print(kmer, kcount[kmer])
	else: print(kmer, 0) 		# any kmer not found has 0 counts

'''
python3 52kmercount.py ecoli.fa.gz 7 | sort -nk2 | head
'''


