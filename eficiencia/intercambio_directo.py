from random import random
from time import time

n = int(input("Ingrese el valor de n: "))
lista = []

#Aleatoria
# for i in range(n):
#   elemento = int(10 * n * random())
#   lista.append(elemento)

#ordenada
for i in range(n):
  elemento = int(10 * n * i)
  lista.append(elemento)

inicio = time()

#Intercambio directo
cambio = True
j = -1
while cambio:
  cambio = False
  j += 1
  for i in range(n - j - 1):
    if lista[i] > lista[i + 1]:
      lista[i],lista[i + 1] = lista[i + 1],lista[i]
      cambio = True
fin = time()

print("Lista ordenada", lista)
print("n =", n, "Duración(SEG): ", fin - inicio)