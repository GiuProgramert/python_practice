from random import random
from time import time

n = int(input("Ingrese el valor de n: "))
lista = []
for i in range(n):
  elemento = int(10 * n * random())
  lista.append()

inicio = time()

#Intercambio directo

fin = time()

print("Lista ordenada", lista)
print("n =", n, "Duración: ", fin - inicio)