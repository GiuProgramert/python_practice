# Calcular el menor elemento en una serie de N números.

print("Calcular el menor elemento en una serie de N números.")

n = int(input('Introduzca la cantidad de números: '))
numero = 0

for i in range(n):
  numero = int(input('Introduzca un número: '))
  if i == 0:
    menor1 = numero
    menor2 = numero

  if numero < menor1 and numero > menor2:
    menor1 = numero
  elif numero < menor1 and numero < menor2:
    if menor1 > menor2 and menor1 > numero:
      menor1 = menor2
      menor2 = numero
    else:
      menor2 = numero
  
print("Los menores son: ", menor1, menor2)
