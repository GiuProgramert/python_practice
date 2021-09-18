print("Almacenar la cantidad de digitos que que tiene el arreglo en cada posición")

n = int(input("Introduzca la cantidad n: "))
lista = []
for i in range(n):
  print("Introduzca los 4 digitos por separador: ")
  cifra1 = int(input())
  cifra2 = int(input())
  cifra3 = int(input())
  cifra4 = int(input())
  lista.append(cifra1)
  lista.append(cifra2)
  lista.append(cifra3)
  lista.append(cifra4)

contador_cifras = [
  0, #Cifra 0 
  0, #Cifra 1
  0, #Cifra 2
  0, #Cifra 3
  0, #Cifra 4
  0, #Cifra 5
  0, #Cifra 6
  0, #Cifra 7
  0, #Cifra 8
  0, #Cifra 9
]
cifras = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(n * 4):
  contador_cifras[lista[i]] = contador_cifras[lista[i]] + 1


for i in range(9):
  for j in range(i + 1, 10):
    if contador_cifras[j] > contador_cifras[i]:
      contador_cifras[i], contador_cifras[j] = contador_cifras[j], contador_cifras[i]
      cifras[i], cifras[j] = cifras[j], cifras[i]

for i in range(10):
  if contador_cifras[i] != 1:
    print("La cifra", cifras[i], "se repite", contador_cifras[i], "veces")
  else:
    print("La cifra", cifras[i], "se repite", contador_cifras[i], "vez")