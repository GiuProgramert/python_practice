n = int(input("Introduzca la cantidad de elementos de la lista: "))
lista = []

for i in range(n):
    lista.append(int(input("Introduzca el elementos de la lista: ")))

x = int(input("Introduzca el valor que desea eliminar de la lista: "))

while i < n:
    if lista[i] == x:
        lista.remove(lista[i])
        n = n - 1
        i = 0
    i = i + 1

print(lista)