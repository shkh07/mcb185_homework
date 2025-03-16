import sys
import sequence
import mcb185


w = 10

seq = 'AAAAAAAAAAGGGGGGGGGGTTTTTTTTTTCCCCCCCCCC'
g = seq[:w].count('G')
c = seq[:w].count('C')
for i in range(len(seq) - w):
	less = seq[i-1]
	more = seq[i + w - 1]
	if less == 'C': c -= 1
	if less == 'G': g -= 1
	if more == 'C': c += 1
	if more == 'G': g += 1
	print(i, sequence.gc_comp(seq[i:i+w]), sequence.gc_skew(seq[i:i+w]))
