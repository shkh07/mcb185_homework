import math

def twopoints(a, b, x, y):
	return math.sqrt(((x - a)**2) + ((y - b)**2))
print("the distance between the two points on the graph is", twopoints(2, 4, 6, 8))

def harmonicmean(n, a, b, c, d):
	return n / ((1/a) + (1/b) + (1/c) +(1/d))
print("the harmonic mean of the four numbers are", (harmonicmean(4, 2, 3, 4, 5)))
