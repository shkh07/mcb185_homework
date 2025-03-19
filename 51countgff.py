import sys
import gzip

'''METHOD 1'''

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1
for f, n in count.items(): print(f, n)

'''METHOD 2'''
count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 1
		else:					count[feature] += 1
for f, n in count.items(): print(f, n)


'''
python3 51countgff.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz
'''

'''
------------------------------------------------------------------------------------------
