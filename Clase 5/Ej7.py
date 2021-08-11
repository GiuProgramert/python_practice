# Encontrar el Máximo Común Divisor entre dos números A y B.

#Entrada de datos
N1 = int(input("Ingrese un número N1: "))
N2 = int(input("Ingrese un número n2: "))

#Cambio de variables para trabajar más comodo en caso de que b > a
if (N2 > N1):
  aux = N1
  N1 = N2
  N2 = aux

#Algoritmo de euclides
resto = N1 % N2
divisor = N2
while resto != 0:
  aux = resto
  resto = divisor % resto
  divisor = aux

#Máximo comun divisor
mcd = aux

#Mínimo comun multiplo
mcm = (N1 * N2) / mcd

print("mcd(N1, N2) = ", mcm)