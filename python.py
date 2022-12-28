import random

test_size = 1_000_000
zeros = 0
ones = 0

for i in range(0, test_size):
    number = random.randint(0, 1)
    if number == 0:
        zeros +=1
    else:
        ones += 1

zeros_percentage = zeros / test_size
ones_percentage = ones /test_size


print(f"Generated {test_size} random samples and got")
print(f"{zeros} ({zeros_percentage :.3%}) zeros and")
print(f"{ones} ({ones_percentage :.3%}) ones.")
