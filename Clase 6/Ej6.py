n = int(input("Introduzca la cantidad de elementos de la lista: "))
lista = []

for i in range(n):
  elemento = int(input(f"Introduzca el elemento {i + 1}: "))
  lista.append(elemento)

for i in range(1, n): 
  if i != n - 1:
    lista[i] = lista[i] + lista[i - 1]

print(lista)