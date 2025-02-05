import random

def roll_d20():
	return random.randint(1, 20)
	
def saving_throw(dc, advantage=False, disadvantage=False):
	rolls = [roll_d20(), roll_d20()]
	if advantage:
		roll= max(rolls)
	elif disadvantage:
		roll = min(rolls)
	else:
		roll = rolls[0]
	print(f"Rolls: {rolls}, Chosen Roll: {roll}, DC: {dc}")
	
	if roll >= dc:
		print('saving throw succesful!')
		return True
	else:
		print('saving throw failed :(')
		return False

print(saving_throw(10, advantage=True))
print(saving_throw(15, disadvantage=True))
print(saving_throw(5))
	