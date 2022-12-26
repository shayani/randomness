import random
zeros = 0
ones = 0

for i in range(0,1000000):
    number = random.randint(0,1)
    if number == 0:
        zeros +=1
    else:
        ones += 1

print(f"Numeros 0:{zeros}, \nNumeros 1:{ones}")
porcentagem_zeros = zeros / 1000000 *100
porcentagem_ones = ones /1000000 *100
print(f"A porcentagem de zeros é: {porcentagem_zeros}%")
print(f"A porcentagem de ones é: {porcentagem_ones}%")