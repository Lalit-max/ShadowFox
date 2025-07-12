import random

# Number of rolls
num_rolls = 20

# Counters
count_6 = 0
count_1 = 0
count_double_6 = 0

# Track previous roll
previous_roll = 0

print("Rolling the die...")

for i in range(num_rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_double_6 += 1
    if roll == 1:
        count_1 += 1

    previous_roll = roll  # Update for next loop

# Results
print("\nStatistics:")
print(f"Total rolls: {num_rolls}")
print(f"Number of times 6 was rolled: {count_6}")
print(f"Number of times 1 was rolled: {count_1}")
print(f"Number of times two 6s were rolled in a row: {count_double_6}")
