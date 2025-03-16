import sys
import math

numbers = [float(num) for num in sys.argv[1:]]

n = len(numbers)

minimum = min(numbers)
maximum = max(numbers)

mean = sum(numbers) / n

variance = sum((x - mean) ** 2 for x in numbers) / n
std_dev = math.sqrt(variance)

sorted_numbers = sorted(numbers)
mid = n // 2
if n % 2 == 0:
	median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
else:
    median = sorted_numbers[mid]
    
print(f'Number of values: {n}')
print(f'Minimum value: {minimum}')
print(f'Maximum value: {maximum}')
print(f'Mean: {mean}')
print(f'Standard Deviation: {std_dev}')
print(f'Median: {median}')



# N50
cumulative_sum = 0
n50 = 0
for num in sorted_numbers:
    cumulative_sum += num
    if cumulative_sum >= total_length / 2:
        n50 = num
        break
        
print(f'Number of values: {n}')
print(f'Minimum value: (minimum}')
print(f'Maximum value: {maximum}')
print(f'Mean: {mean}')
print(f'Standard Deviation: {std_dev}')
print(f'Median: {median}')
print(f'N50: {n50}')