import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

fin = 0
for i in range(trials):
	in_bday = []
	for i in range(people):
		person = random.randint(0, days-1)
		in_bday.append(person)
	
	for j in in_bday:
		rep = in_bday.count(j)
		if rep > 1:
			fin += 1
			break
			
print(fin / trials)
		