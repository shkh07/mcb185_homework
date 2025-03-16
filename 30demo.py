

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
print('hey "dude" don\'t tell me what to do')

print(s.count(s1))
print(s.endswith(s1))
print(s.startswith(s1))
print(s.upper())
print(s.lower())
print(s.rstrip())
print(s.replace('o', ''))

import math

print(f'{math.pi}')            
print(f'{math.pi:.3f}')        
print(f'{1e6 * math.pi:e}')    
print(f'{"hello world":>20}')  
print(f'{"hello world":.>20}') 
print(f'{20:<10} {10}')        

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-6])
for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
a = 'ABCDEFGHIJ'
print(a[0:5])
print(a[0:8:2])

print(a, a[::], a[::1], a[::-1])

tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0])
print(tax[::-1])

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIJHLMNOPQRSTUVWXYZ'
print(alph)
aas = list(alph)
print(aas)

text = 'good day		to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s= '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
print('index Z', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

vals = ('butter', 'cookie', 'milk', 'apple')

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
def minmax(vals):
	mini = vals[0]
	maxi = vlas[0]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

import math

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))


import sys
print(sys.argv)

i = int('42')
x = float('0.61803')
print(i * x)

for nt in seq:
    print(nt, end='')
print()

for i in range(len(seq)):
    print(i, seq[i])

def print_codons(sequence):
	for i in range(0, len(sequence) - 2, 3):
		position = i + 1
		codon = sequence[i:i+3]
		frame = (position - 1) % 3 + 1
		print(f"{position}\t{frame}\t{codon}")
sequence = 'ATGCTGTAA'
print_codons(sequence)