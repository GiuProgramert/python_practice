from random import random

n = 1000
c_cara = 0
c_cruz = 0

for i in range(n):
  lanzamiento = int(2 * random())
  if lanzamiento == 1:
    c_cruz = c_cruz + 1
  else:
    c_cara = c_cara + 1

print("Cantidad de lanzamientos que salieron cara: ", c_cara, "\nCantidad de lanzamientos que salienron cruz: ", c_cruz)