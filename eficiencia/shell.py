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

#Shell
salto = int(n / 2)
while salto >= 1:
  cambio = False
  i = 0
  while (i + salto) <= (n - 1):
    if lista[i + salto] < lista[i]:
      lista[i], lista[i + salto] = lista[i + salto], lista[i]
      cambio = True
    i = i + 1
  
  if not cambio:
    salto = int(salto / 2)
      

fin = time()

print("Lista ordenada", lista)
print("n =", n, "Duración(SEG): ", fin - inicio)