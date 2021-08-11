# Encontrar el Máximo Común Divisor entre dos números A y B.

#Entrada de datos
a = int(input("Ingrese un número A: "))
b = int(input("Ingrese un número B: "))

#Cambio de variables para trabajar más comodo en caso de que b > a
if (b > a):
  aux = a
  a = b
  b = aux

#Algoritmo de euclides
resto = a % b
divisor = b
while resto != 0:
  aux = resto
  resto = divisor % resto
  divisor = aux

#salida
mcd = aux
print("mcd(A, B) = ", mcd)
