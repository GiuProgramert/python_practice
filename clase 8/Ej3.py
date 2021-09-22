from random import random

n = int(input("Ingrese la cantidad de veces que se lanzara una moneda: "))

# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1

iguales = 0
for i in range(n):
  M1 = int(2 * random())
  M2 = int(2 * random())
  M3 = int(2 * random())
  if M1 == M2 and M2 == M3:
    iguales += 1
  
probabilidad = iguales / n
print("La probabilidad de que salgan caras y cruces son: ", probabilidad)