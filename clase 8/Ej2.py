from random import random

n = int(input("Introduzca un valor de N: "))
c_cara = 0
c_cruz = 0

for i in range(n):
  lanzamiento = int(2 * random())
  if lanzamiento == 1:
    c_cruz = c_cruz + 1
  else:
    c_cara = c_cara + 1

print("La probabilidad de apararicion de cara es: ", c_cara / n)
print("La probabilidad de apararicion de cruz es: ", c_cruz / n) 

#A medida que aumenta N la probabilidad se aproxima a 50% de cruz y 50% de cara