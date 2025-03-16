import sys
import mcb185
import math

w = int(sys.argv[2])
e = float(sys.argv[3])


def entropy(a, c, g, t):
	greater_zero = []
	total = 0
	for ct in [a, c, g, t]:
		if ct > 0: 
			greater_zero.append(ct)
			total += ct
	h = 0
	for ct in greater_zero:
			p = ct / total
			h -= p * math.log2(p)
	return h
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)
	data = []
	for i in range(0, len(seq) - w + 1, w):
		s = seq[i:i+w]
		nts = 'ACGT'
		counts = [0] * len(nts)
		for nt in s:
			idx = nts.find(nt)
			counts[idx] += 1
		A = counts[0]
		C = counts[1]
		G = counts[2]
		T = counts[3]
		total = (A + C + G + T)
		g = []
		for count in [A, C, G, T]:
			if count > 0: g.append(count)
		ent = 0
		for count in g:
			p = count / total
			ent -= p * math.log2(p)
			h = ent
		if h < e:
			for j in range(len(s)):
				data.append('N')
		else:
			data.append(s)
	data = ''.join(data)
	print(data[:300])
