# 10demo.py by Sohail Khan

print ('hello, again') # greeting

"""
This is a multi line comment
"""

print (1.5e-2)
print(1+1)
print(1-1)
print(2*2)
print(1/2)
print(2**3)
print(5//2)
print(5%2)
print(5*(2+1))

print(abs(-4))
print(pow(4,2))
print(round(4,ndigits=3))

import math

print(math.ceil(5))
print(math.floor(5))
print(math.log(2))
print(math.log2(2))
print(math.log10(2))
print(math.sqrt(25))
print(math.pow(4,2))
print(math.factorial(24))
print(math.e)
print(math.pi)
print(math.inf)
print(math.nan)

print(0.1*1)
print(0.1*3)

a = 3							# side of triangle
b = 4							# side of triangle
c = math.sqrt(a**2 + b**2)		# hypotenuse
print("the long way", c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b):
	c = math.sqrt(a**2 +b**2)
	return c
	
hyp = pythagoras(5, 4)
h2 = pythagoras(3, 9)
print("function", hyp, h2)

def pythagoras2(a,b):
	return math.sqrt(a**2 +b**2)
print("function2", pythagoras2(2, 5))

def fahrenheitcelsius(f):
	return (f - 32) * 5 / 9
print("the degrees in celsius is", fahrenheitcelsius(80))

def circle_area(r):
	return math.pi * r**2
print ("the circle area is", circle_area(2))

def rectangle_area(w, h):
	return w * h
print ("the area of the rectangle is", rectangle_area(4, 5))

def triangle_area(w, h):
	return (w * h) / 2
print ("the area of the triangle is", triangle_area(4, 5))

def armean(a, b, c):
	return (a + b + c) / 2
print ("the mean is", armean(4, 5, 20))

s = 'hello world'
print(s, type(s))

a = 4
b = 2
if a != b:
	print('a dpes not equal b')
print(a, b)

def is_even(x):
	if x % 2 == 0: return True
	return False
print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

a = 26
b= 43
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4))

# Extra Practice For ME

def FC(a):
	return (a-32)*5/9
print('the temperate in celsius is', FC(32))

def KM(a):
	return (a/1.60934)
print('the speed of 36 kmh in mph is', KM(100))

def conc(a):
	return a * 0.8 * 50
print('the dna concentration is', conc(25))
print(type(a))

def maximum(a, b, c):
	return max(a, b, c)
print(maximum(4, 5, 6))

def sensitivity(tp, fn):
	if tp + fn == 0: return 0
	return tp / (tp + fn)
print(sensitivity(5, 6))

def specificity(tn, fp):
	if tn + fp == 0: return 0
	return tn / (tn + fp)
print(specificity(5, 5))


def f1_score(tp, fp, fn):
    if tp == 0: return 0
    precision = tp / (tp + fp) if (tp + fp) != 0 else 0
    recall = tp / (tp + fn) if (tp + fn) != 0 else 0
    if precision + recall == 0: return 0
    return 2 * (precision * recall) / (precision + recall)
print(f1_score(5, 6, 8))

def shannon_entropy(a, c, g, t):
	total = a + c + g + t
	if total == 0: return 0
	probabilities = [n / total for n in (a, c, g, t) if n > 0]
	return -sum(p * math.log2(p) for p in probabilities)
print(shannon_entropy(20, 15, 30, 20))	

def is_integer(n):
	return n % 1 == 0
print(is_integer(5))

def probability(p):
	return 0 <= p <=1
print(probability(0.5))

def weight(letter):
	weights = {'A': 313.2, 'C': 289.2, 'G': 329.2, 'T': 304.2}
	return weights.get(letter.upper(), None)
print(weight('X'))

def complement(letter):
	complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	return complements.get(letter.upper(), None)
print(complement('A'))

def maximum(a, b, c):
	return max(a, b, c)
print(maximum(5, 9, 12))

# PHRED quality scores use the formula -10 * log10(p) to measure the base call accuracy
# which has a higher score that also allows a lower error probability. Thus, if needed,
# we can modify the program for log2 by -5 * log2(p) for a similar probability scale.