# Calcular el menor elemento en una serie de N números.

print("Calcular el menor elemento en una serie de N números.")

numero = int(input('Introduzca un númeroo introduzca -1 para finalizar: '))
mayor = 0

while numero != -1:
  if numero > mayor:
    mayor = numero

  numero = int(input('Introduzca un número o introduzca -1 para finalizar: '))

print("El mayor es: ", mayor)
