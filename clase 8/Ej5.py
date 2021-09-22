# Para realizar la prueba de un algoritmo se necesita tener una lista de 50 números cuyos valores deben estar
# comprendidos entre 750 y 2400 sin que existan números repetidos. Escribir un algoritmo que genere estos números,
# los almacene en un vector de 50 componentes y luego imprima este vector.
from random import random

lista = []
long_lista = 0

for i in range(50):
  cambio = False
  while cambio == False:
    cambio = True
    numero = int(2400 * random())
    existe = False
    for j in range(long_lista):
      if lista[j] == numero:
        existe == True
    if 750 > numero or numero > 2400 or existe:
      cambio = False
  
  lista.append(numero)
  long_lista += 1

print(lista)