def tm(A, C, G, T):
	if A + C + G + T <= 13:
		return (A + T) * 2 + (G + C) * 4
	else: 
		return 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)
print(tm(5, 7, 3, 4))

		