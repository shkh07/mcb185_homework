import random

trials = 1000
stab = 0
die = 0
rev = 0
for i in range(trials):
	succSesses = 0
	fails = 0
	revived = False
	
	while successes < 3 and fails < 3 and revived == False:
		roll = random.randint(1,20)
		
		if roll == 20:
			revived = True
		elif roll >= 10:
			successes += 1
		elif roll == 1: # natural 1
			fails += 2
		else: # roll failed but not a 1
			fails += 1
	if revived:				rev += 1
	elif successes >= 3: 	stab += 1
	else: 					die += 1
	
print(successes, fails, revived)
print('revived:', rev, 'stabilized:', stab, 'died:', die)
print('revived:', rev / trials, 'stabilized:', stab / trials, 'died:', die / trials)
print('total good cases:', (rev / trials) + (stab / trials))