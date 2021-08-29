print("Desplazar los elementos de una lista a la derecha")

n = int(input("Introduzca la cantidad de elementos\n"))
lista = []

print("Introduzca los elementos de la lista")
for i in range(n):
  elemento = int(input())
  lista.append(elemento)

print("Lista inicial: ", lista)
for i in range(n - 1, 0, -1):
  print(lista)
  if i == (n - 1):
    lista[0], lista[n - 1] = lista[n - 1], lista[0]
  else:
    lista[i], lista[i + 1] = lista[i + 1], lista[i]
print("Lista final: ", lista)
