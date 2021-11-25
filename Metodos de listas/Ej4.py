lista = []

n = int(input("Ingrese la cantidad de elementos de la lista: "))
p = int(input("Ingrese la cantidad de posiciones que se va a mover la lista: "))

for i in range(n):
    lista.append(int(input("Ingrese el elemento de la lista: ")))

movimientos = 0
if p <= n:
    movimientos = p
else:
    movimientos = p % n

for i in range(movimientos):
    elemento = [lista.pop()]
    elemento.extend(lista)
    lista = elemento.copy()

print(lista)