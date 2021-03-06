# Utilizando la capacidad de generar números al azar, imprimir la lista de todos los números de 5 cifras que pueden formarse utilizando
# los dígitos: 1, 2, 3, 4 y 5. Cada dígito puede aparecer una sola vez y solo pueden aparecer dichos dígitos. Ejemplos: 12345, 34152,
# 45132, etc. (Observación: son 120 números distintos)
from random import random

numeros = []

i = 0
while i < 120:
  numeros_individuales = []
  long_numeros = 0

  for j in range(5):
    cambio = False
    while cambio == False:
      cambio = True
      numero_individual = int(5 * random()) + 1
      existe = False
      if numero_individual in numeros_individuales:
        existe = True
      if existe:
        cambio = False
    numeros_individuales.append(numero_individual)
    long_numeros += 1

  numero = 0
  incrementador = 10
  for j in range(5):
    numero = numero + (numeros_individuales[j] * incrementador ** j)
  if numero not in numeros:
    numeros.append(numero)
    i = i + 1

numeros.sort()

print("Cantidad:", i)
print(numeros)