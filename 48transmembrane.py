import sys
import mcb185

def calc(window):
	hydrop = 0

	amino = 'ACDEFGHIKLMNPQRSTVWY'
	aminohs = [1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, 
			  -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3]
	
	for aa in range(len(window)):
		hydrop += aminohs[amino.find(window[aa])]
	
	return hydrop/len(window)


def hp(seq, w, t):
	signal = False
	for i in range(len(seq) - w + 1):
		win = seq[i: i + w]
		if 'P' in win: continue
		elif calc(win) < t: continue
		else:
			return True
	return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	name = words[0]
	if hp(seq[0:30], 8, 2.5) and hp(seq[30:], 11, 2.0):
		print(defline)
		
		