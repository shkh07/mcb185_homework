import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d	

mini = 1000

with open(colorfile) as fp:
	for line in fp:
		words = line.split()
		name = words[0]
		for i in words:
			col = words[2].split(',')
			rgb = (int(col[0]), int(col[1]), int(col[2]))
		d = dtc([R,G,B],rgb) 
		if d < mini:
			mini = d
			closest = name
		
print(closest)

'''
python3 45colorname.py ~/Code/MCB185/data/colors_extended.tsv 200 0 50
'''
