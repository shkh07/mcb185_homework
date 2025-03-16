import sys

alphabet = sys.argv[1]
match_score = int(sys.argv[2])
mismatch_score = int(sys.argv[3])

print("   " + " ".join(alphabet))

for i, char1 in enumerate(alphabet):
    row = [char1]
    for j, char2 in enumerate(alphabet):
        if i == len(alphabet) - 1 and j == len(alphabet) - 1:
            row.append("-1")
        else: 
            if char1 == char2: score = match_score
            else: score = mismatch_score
            row.append(f"{score:+}")
    print(" ".join(row))
    
    
    
    
    
    