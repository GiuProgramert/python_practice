print("Hallar k en un vector X")

x = int(input("Introduzca la longitud X de la lista: "))
k = int(input("Introduzca el valor K a buscar en la lista: "))
lista = []

for i in range(x):
  elemento = int(input(f"Introduzca el elemento {i + 1}: "))
  lista.append(elemento)

#b) La lista tiene elementos repetidos y se busca la primera aparición del valor.
encontrado = False
posicion = -1 #Si cargo 0 puede confundirse con el indice 0 de la lista.
i = 0
while not encontrado:
  if lista[x - 1] == k:
    encontrado = True
    posicion = x
  else:
    if lista[i] == k:
      if lista[i] != lista[i + 1]:
        encontrado = True
        posicion = i + 1
    i = i + 1

if encontrado:
  print("Elemento encontrado en la posición:", posicion)
else:
  print("Elemento no encontrado")