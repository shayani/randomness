import random
<<<<<<< HEAD
zeros = 0
ones = 0

for i in range(0,1000000):
    number = random.randint(0,1)
=======

test_size = 1_000_000
zeros = 0
ones = 0

for i in range(0, test_size):
    number = random.randint(0, 1)
>>>>>>> 517d958 (add script python)
    if number == 0:
        zeros +=1
    else:
        ones += 1

<<<<<<< HEAD
print(f"Numeros 0:{zeros}, \nNumeros 1:{ones}")
porcentagem_zeros = zeros / 1000000 *100
porcentagem_ones = ones /1000000 *100
print(f"A porcentagem de zeros é: {porcentagem_zeros}%")
print(f"A porcentagem de ones é: {porcentagem_ones}%")
=======
zeros_percentage = zeros / test_size
ones_percentage = ones /test_size

print(f"Generated {test_size} random samples and got")
print(f"{zeros} ({zeros_percentage :.3%}) zeros and")
print(f"{ones} ({ones_percentage :.3%}) ones.")
>>>>>>> 517d958 (add script python)
