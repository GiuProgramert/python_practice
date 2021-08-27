n = int(input("Ingrese la cantidad de elementos de la lista:\n"))
contador_ceros = 0
lista = []

for i in range(n):
  elemento = int(input(f"Introduzca el elemento {i + 1} de la lista: "))
  if elemento == 0:
    contador_ceros += 1
  lista.append(elemento)

#Agrega los elementos que no son cero
lista_cambiada = []
for elemento in lista:
  if elemento != 0:
    lista_cambiada.append(elemento)

#Agrega la cantidad de ceros al final
for i in range(contador_ceros):
  lista_cambiada.append(0)

print(lista_cambiada)