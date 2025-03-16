import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

fin = 0
for i in range(trials):
    calendar = [0] * days

    for i in range(people):
        birthday = random.randint(0, days - 1)
        calendar[birthday] += 1

        if calendar[birthday] > 1:
            fin += 1
            break

print(fin / trials)
