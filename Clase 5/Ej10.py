# Calcular el menor elemento en una serie de N números.

print("Calcular el menor elemento en una serie de N números.")

n = int(input('Introduzca la cantidad de números: '))
numero = 0

for i in range(n):
  numero = int(input('Introduzca un número: '))
  if i == 0:
    menor = numero
  
  if numero < menor:
    menor = numero
  
print("El menor es: ", menor)
