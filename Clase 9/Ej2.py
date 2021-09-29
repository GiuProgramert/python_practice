n = int(input("Introduzca la cantidad de valores de la lista: "))
p = int(input("Introduzca hasta donde la lista estara ordenada: "))
k = int(input("Introduzca el elemento que desea insertar en la lista: "))

numeros = []
for i in range(n):
  numero = int(input("Introduzca un número: "))
  numeros.append(numero)

#ordenar la lista hasta p por método shell
salto = int(p / 2)
while salto >= 1:
  i = 0
  cambio = False
  while (i + salto) <= (p - 1):
    if numeros[i] > numeros[i + salto]:
      numeros[i], numeros[i + salto] = numeros[i + salto], numeros[i]
      cambio = True
    i = i + 1
  
  if not cambio:
    salto = int(salto / 2)

#Encontrar la posición del elemento que este antes de k
inicio = 0
fin = p - 1
pos_k = -1
medio = int((inicio + fin) / 2)
while numeros[medio] != k and inicio <= fin:
  if numeros[medio] > k:  
    fin = medio - 1
  else:
    inicio = medio + 1
  medio = int((inicio + fin) / 2)

#Guardar la posicion donde deberia ir k
if numeros[medio] + 1 == k:
  pos_k = medio + 1

#Mover los elementos para que puede entrar k
for i in range (n - 1, pos_k, -1): 
  numeros[i], numeros[i - 1] = numeros[i - 1], numeros[i]

#Insertar k
numeros[pos_k] = k

print(numeros)