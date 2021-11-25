n = int(input("Introduzca la cantidad de elementos de la lista: "))
l1 = []

for i in range(n):
    l1.append(int(input("Introduzca el elementos de la lista: ")))

l2 = []

l1_copia = l1.copy()
l1_copia.sort()

for i in range(n):
    l2.append(l1_copia.index(l1[i]))

print(l2)