n = int(input("Introduzca la cantidad de elementos de la lista: "))
p = int(input("Introduzca la cantidad de lugares que se van a desplazar: "))
lista = []

for i in range(n):
  elemento = int(input(f"Introduzca el elemento {i + 1}: "))
  lista.append(elemento)

print("Lista original: ", lista)

for i in range(p):
  ultimo_elemento = lista[n - 1]
  for j in range(n - 1, 0, -1):
    aux = lista[j]
    lista[j] = lista[j - 1]
    lista[j - 1] = aux
  lista[0] = ultimo_elemento

print("Lista final: ", lista)