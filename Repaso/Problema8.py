print("Ordenar de forma ascendente los pares y descendente los impares")

n = int(input("Introduzca el valor de la lista N: "))
lista = []
for i in range(n):
  elemento = int(input("Introduzca un elemento de la lista: "))
  lista.append(elemento)

pares = []
long_pares = 0
impares = []
for i in range(n):
  if lista[i] % 2 == 0:
    pares.append(lista[i])
    long_pares = long_pares + 1
  else:
    impares.append(lista[i])

cambio = True
j = -1 
while cambio == True:
  cambio = False
  j = j + 1
  for i in range(long_pares - j - 1):
    if pares[i + 1] < pares[i]:
      pares[i], pares[i + 1] = pares[i + 1], pares[i]
      cambio = True

cambio = True
j = -1 
while cambio:
  cambio = False
  j += 1
  for i in range((n - long_pares) - j - 1):
    if lista[i + 1] < lista[i]:
      lista[i], lista[i + 1] = lista[i + 1], lista[i]
      cambio = True

lista_ordenada = []

for i in range(long_pares):
  lista_ordenada.append(pares[i])

for i in range(n - long_pares):
  lista_ordenada.append(impares[i])

print("La lista sin ordenar es: ", lista)
print("La lista ordenada es", lista_ordenada)