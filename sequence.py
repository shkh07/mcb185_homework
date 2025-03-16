# Transcribing

def transcribe(dna):
	return dna.replace('T', 'U')
	
# Reverse Complement

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)
	
# Translation

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)
	
def translate(dna):
	codons = ('ATG', 'TAA', 'TAG', 'TGA')
	aminos = 'M***'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons: # checks if the codon is one of the recognized ones
			idx = codons.index(codon) # finds the position of the codon in codons tuple
			aa = aminos[idx] # uses the position to find the amino acid in aminos
			aas.append(aa) # amino acid is appended to aas
		else:
			aas.append('X')
	return ''.join(aas)
	
# GC comp

def gc_comp(seq):
    return (seq.count('C') + seq.count('G')) / len(seq)
    
# GC Skew

def gc_skew(seq):
    c = seq.count('C')
    g = seq.count('G')
    if c + g == 0: return 0
    return (g - c) / (g + c)