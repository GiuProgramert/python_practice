na = int(input("Introduzca la cantidad de elementos de A: "))
nb = int(input("Introduzca la cantidad de elementos de B: "))

lista_A = []
lista_B = []

for i in range(na):
  elemento = int(input("Introduzca un elemento en la lista A: "))
  lista_A.append(elemento)

for i in range(nb):
  elemento = int(input("Introduzca un elemento en la lista B: "))
  lista_B.append(elemento)

#Ordenar A y B
for i in range(na - 1):
  for j in range(i + 1, na):
    if lista_A[j] < lista_A[i]:
      lista_A[i], lista_A[j] = lista_A[j], lista_A[i]

for i in range(nb - 1):
  for j in range(i + 1, nb):
    if lista_B[j] < lista_B[i]:
      lista_B[i], lista_B[j] = lista_B[j], lista_B[i]

#Agregar a la lista C
lista_C = []
for i in range(na):
  lista_C.append(lista_A[i])

for i in range(nb):
  lista_C.append(lista_B[i])

existe = False
for i in range(na + nb):
  if lista_C[i] == 225:
    existe = True
  
if existe:
  print("Existen el número 225")
else:
  print("No existe el número 225")

for i in range((na + nb) - 1):
  for j in range(i + 1, na + nb):
    if lista_C[j] < lista_C[i]:
      lista_C[i], lista_C[j] = lista_C[j], lista_C[i]

print("La lista C es: ", lista_C)