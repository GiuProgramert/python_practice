n = int(input("Introduzca la cantidad de valores de la lista: "))
p = int(input("Introduzca hasta donde la lista estara ordenada: "))
k = int(input("Introduzca el elemento que desea buscar en la lista: "))

numeros = []
for i in range(n):
  numero = int(input("Introduzca un número: "))
  numeros.append(numero)

#ordenar la lista hasta p
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
#Busqueda secuencial para ver si es encontrado k en los elementos ordenados
pos_k = -1
inicio = 0
fin = p - 1
medio = int((inicio + fin) / 2)
while numeros[medio] != k and inicio <= fin:
  if numeros[medio] > k:
    fin = medio - 1
  else:
    inicio = medio + 1
  medio = int((inicio + fin) / 2)

if numeros[medio] == k:
  pos_k = medio

print(numeros)
if pos_k != -1:
  print("Elemento en posición", pos_k, "Encontrado por busqueda binaria")
else:
  #busqueda secuancial si k no esta en los elementos ordenados los buscamos en la parte no ordenada
  i = p
  while pos_k == -1 and i < n:
    if numeros[i] == k:
      pos_k = i
    i = i + 1
  print("Elemento en posición", pos_k, "Encontrado por busqueda secuencial")