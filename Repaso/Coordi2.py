print("||Escribir los N primeros números de la serie de Fibonacci||")

n = int(input('Introduzca N: \n'))

serie = []
for i in range(n):
  if i == 0 or i == 1:
    serie.append(1)
  else:
    serie.append(serie[i - 1] + serie[i -2])

print("fibunacci(", n, ") = ", serie[n - 1])