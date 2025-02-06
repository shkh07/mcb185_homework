import random

def saving_throws(dc, mode):
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	
	if mode == 'advantage':
		roll = (roll1, roll2)
		if roll1 > roll2:
			roll = roll1
		else:
			roll = roll2
	elif mode == 'disadvantage':
		roll = (roll1, roll2)
		if roll1 < roll2:
			roll = roll1
		else:
			roll = roll2
	else:
		roll = roll1
	
	if roll >= dc: return 'success'
	else: return 'no success'

print(saving_throws(10, 'disadvantage'))
print(saving_throws(21, 'disadvantage'))