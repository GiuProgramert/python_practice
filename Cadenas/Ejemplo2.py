print("Dabe un número determinar si es capicua")

numeros = input("Introduzca el número: ")

inicio = 0
fin = len(numeros) - 1

es_capicua = True
while inicio < fin:
  if numeros[inicio] != numeros[fin]:
    es_capicua = False
  
  inicio += 1
  fin -= 1

if not es_capicua:
  print("No es capicua")
else:
  print("Es capicua")