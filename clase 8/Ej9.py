from random import random

numeros = []
i = 0

while i < (70 - 31):
    numero = int(70 * random()) + 1
    if numero not in numeros and numero > 31:
        numeros.append(numero)
        i += 1 

print(numeros)