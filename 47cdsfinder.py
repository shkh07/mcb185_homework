import sys
import mcb185
import sequence

def get_protein(seq, t):
	proteins = []
	for i in range(3):
		translation = mcb185.translate(seq[i:])
		orfs = translation.split('*')
		for orf in orfs:
			if 'M' not in orf: continue
			idx = orf.index('M')
			pro = orf[idx:]
			if len(pro) >= t: proteins.append(pro)
	return proteins


	
min_length = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	p = 0
	for protein in get_protein(seq, min_length):
		print(f'>{name}-prot-{p}')
		print(protein)
		p += 1
