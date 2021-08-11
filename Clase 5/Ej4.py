# Encontrar el número entero N tal que la suma de todos los enteros de 1 hasta N es igual a 10
# veces el valor de N.

n = 1
suma = 1

while suma != (n * 10):
  n += 1
  print(suma)
  suma += n

print(f"\nEl valor de N es: {suma}")