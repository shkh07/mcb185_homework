import random

def saving_throws(trials): # function for simulating throws
	dc5 = 0 # successes for dc5
	dc10 = 0
	dc15 = 0
	failures = 0 # count rolls below dc 5

	for i in range(trials):
		roll = random.randint(1, 20)
		
		# gonna look for the highest dc first
		if roll >= 5:
			dc5 += 1
		elif roll >= 10:
			dc10 += 1
		elif roll >= 15:
			dc15 +1
		else:
			failures += 1
	print(dc5 / trials)
	print(dc10 / trials)
	print(dc15 / trials)
	print(failures / trials)
print(saving_throws(100000)) # running the program with 100000 trials
	