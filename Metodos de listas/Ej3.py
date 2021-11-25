n1 = int(input("Introduzca la cantidad de elementos de la lista 1: "))
lista1 = []

for i in range(n1):
    lista1.append(int(input("Introduzca el elementos de la lista 1: ")))

n2 = int(input("Introduzca la cantidad de elementos de la lista 2: "))
lista2 = []

for i in range(n2):
    lista2.append(int(input("Introduzca el elementos de la lista 2: ")))

lista3 = []

for i in range(n1):
    if lista1[i] in lista1 and lista1[i] in lista2 and lista1[i] not in lista3:
        lista3.append(lista1[i])

print("La union de las listas es:", lista3) 