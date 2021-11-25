from random import random
from time import time

n = int(input("Ingrese el valor de n: "))
lista = []

#Aleatoria
for i in range(n):
  elemento = int(10 * n * random())
  lista.append(elemento)

#ordenada
# for i in range(n):
#   elemento = int(10 * n * i)
#   lista.append(elemento)

inicio = time()

#Selección directa
for i in range(n - 1):
  for j in range(i + 1, n):
    if lista[j] < lista[i]:
      lista[i], lista[j] = lista[j], lista[i]

fin = time()

print("Lista ordenada", lista, end="\n\n")
print("N =", n, "Duración(SEG): ", fin - inicio)