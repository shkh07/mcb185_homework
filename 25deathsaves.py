import random

def simulate_death_save():
    failures = 0
    successes = 0
    
    while failures < 3 and successes < 3:
        roll = random.randint(1, 20)
        
        if roll == 1:
            failures += 2  # Critical failure
        elif roll == 20:
            return "Revived"  # Immediate revival
        elif roll < 10:
            failures += 1
        else:
            successes += 1
            
        if failures >= 3:
            return "Died"
        if successes >= 3:
            return "Stable"

def estimate_probabilities(trials=100000):
    outcomes = {"Died": 0, "Stable": 0, "Revived": 0}
    for _ in range(trials):
        outcome = simulate_death_save()
        outcomes[outcome] += 1
    for key in outcomes:
        outcomes[key] /= trials
    return outcomes

probabilities = estimate_probabilities()
print(probabilities)