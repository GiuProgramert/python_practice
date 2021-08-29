# Para determinar si dos listas de H valores están formadas exactamente por los mismos números, se
# pide ingresar cada lista por separado y luego verificar si sus respectivos contenidos son iguales.

h = int(input("Ingrese el valor de H\n"))

lista_a, lista_b = [], []

for i in range(h):
  elemento = int(input("Introduzca un elemento de A: "))
  lista_a.append(elemento)

for i in range(h):
  elemento = int(input("Introduzca un elemento de B: "))
  lista_b.append(elemento)

for i in range(h - 1):
  for j in range(i + 1, h):
    if lista_a[i] > lista_a[j]:
      lista_a[i], lista_a[j] = lista_a[j], lista_a[i]
    
    if lista_b[i] > lista_b[j]:
      lista_b[i], lista_b[j] = lista_b[j], lista_b[i]

contador = 0
#Verificar si son iguales
for i in range(h):
  if lista_a[i] == lista_b[i]:
    contador += 1

if contador == h:
  print("Ambos vectores son iguales")
else:
  print("Las listas no son iguales")