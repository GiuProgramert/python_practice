m = int(input("Introducir la cantidad m de elementos: "))
n = int(input("Indicar de cuanto en cuanto debemos tomar: "))

def factorial(numero):
  acumulador = 1
  for i in range(numero, 0, -1):
    acumulador = acumulador * i
  return acumulador

combinaciones = factorial(m) / (factorial(n) * factorial(m - n))
print("La cantidad de combinaciones es: ")