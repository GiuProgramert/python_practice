def poner_no_repetidos(lista, n, no_repetidos):
    for i in range(n):
        if lista[i] not in no_repetidos:
            no_repetidos.append(lista[i])

    return no_repetidos    

#!Agregar inputs
#---------------
#---------------

lista1 = [9, 4, 3, 2, 4, 7, 4, 7, 2, 9, 8, 8, 1, 8]
n1 = len(lista1)

lista2 = [4, 7, 9, 5, 8, 1, 6]
n2 = len(lista2)

no_repetidos = []
no_repetidos = poner_no_repetidos(lista1, n1, no_repetidos)
no_repetidos = poner_no_repetidos(lista2, n2, no_repetidos)

no_repetidos.sort()

print(lista1)
print(lista2)
print(no_repetidos)