print("Hallar k en un vector X")

x = int(input("Introduzca la longitud X de la lista: "))
k = int(input("Introduzca el valor K a buscar en la lista: "))
lista = []

for i in range(x):
  elemento = int(input(f"Introduzca el elemento {i + 1}: "))
  lista.append(elemento)

#a) la lista no tiene elementos repetidos
encontrado = False
posiciones = []
for i in range(x):
  if lista[i] == k:
    encontrado = True
    posiciones.append(i + 1)

if encontrado:
  print("Elemento encontrado en las posiciónes:", posiciones)
else:
  print("Elemento no encontrado")