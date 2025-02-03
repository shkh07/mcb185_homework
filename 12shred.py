import math

def char_to_prob(char):
	q = ord(char) - 33
	return 10 ** (-q / 10)
print(char_to_prob('A'))

def char_to_prob(char):
	q = ord(char) - 33
	return 10 ** (-q / 10)
print(char_to_prob('?'))

def prob_to_char(prob):
	phred_score = -10 * math.log10(prob)
	return chr(int(phred_score) + 33)
print(prob_to_char(0.001))

def prob_to_char(prob):
	phred_score = -10 * math.log10(prob)
	return chr(int(phred_score) + 33)
print(prob_to_char(0.05))

def prob_to_char(prob):
	phred_score = -10 * math.log10(prob)
	return chr(int(phred_score) + 33)
print(prob_to_char(0.008))
	