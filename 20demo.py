
t = 1, 2 # this is a tuple
print(t)
print(type(t))

person = 'steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) /2
	return x, y
print(midpoint(5, 6, 7, 8))

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)
print(m[0], m[1])


i = 0
while True:
	i = i + 1
	print('hey', i)
	if i ==3: break

i=0
while i < 3:
	i = i + 1
	print('hey', i)

i = 0
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)
	
for i in range(5): print(i)
for i in range(0,5): print(i)
for i in range(0, 5, 1): print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
for i in range(len(basket)):
	print(basket[i])

for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else: print(i, 'is odd')

# Practice Problems

import math 

def triangular(n):
	return n * (n+1) // 2
print(triangular(5))

def triangular2(n):
	tri = 0
	for i in range(n+1):
		tri = tri + i
	return tri
print(triangular2(5))

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
print(factorial(5))

def poisson(n, k):
	return n**k * math.e**-n / factorial(k)
print(poisson(4, 6))

def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))
print(nchoosek(47, 6))

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e
print(euler(1))

def is_prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False
	return True
print(is_prime(7))

def nilakantha(limit):
	pi = 3
	for i in range(1, limit+1):
		n = 2 * i
		d = n * (n+1) * (n+2)
		if i % 2 == 0: pi = pi - 4 / d
		else: pi = pi + 4 / d
	return pi
	
import random

for i in range(5):
	print(random.random())
	
for i in range(3):
	print(random.randint(1, 6))
	
# More Practice

import random
import math

def estpi():
	inside = 0
	total = 0
	while True:
		x, y = random.random(), random.random()
		distance = math.sqrt(x**2 + y**2)
		if distance < 1: inside += 1
		total += 1
		estpi = (inside / total) * 4
print('estimated pi', estpi())
		