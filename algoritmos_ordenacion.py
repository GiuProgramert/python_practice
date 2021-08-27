from random import randint
from time import time

def metodo_seleccion_directa(lista):
    for i in range (n-1):
        for j in range(i + 1, n):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    print(lista)

def metodo_burbuja(lista):
    cambio = True
    j = -1 
    while cambio:
        cambio = False
        j += 1
        for i in range(n-j-1):
            if lista[i + 1] < lista[i]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                cambio = True
    print(lista)

def metodo_shell(lista):
    salto = int(n / 2)

    while salto >=1:
        i = 0
        cambio = False
        while (i + salto) <= (n - 1):
            if lista[i] > lista[i + salto]:
                lista[i], lista[i + salto] = lista[i + salto], lista[i]
                cambio = True
            i = i + 1

        if not cambio:
            salto = int(salto / 2)
    print(lista)

print("Ordenar una lista por método burbuja")
n = int(input("Ingrese el tamaño de la lista: "))
lista = []

for i in range(n):
    # elemento = int(input(f"Introduzca el elemento {i + 1} de la lista: "))
    elemento = randint(0, 10000)
    lista.append(elemento)

print("La lista sin ordenar es: ", lista)

start = time()
metodo_seleccion_directa(lista)
tiempo1 = time() - start

start = time()
metodo_burbuja(lista)
tiempo2 = time() - start

start = time()
metodo_shell(lista)
tiempo3 = time() - start

tiempos = [tiempo1, tiempo2, tiempo3]

menor = tiempos[0]
indice_menor = 0
for i in range(3):
    print(tiempos[i])
    if tiempos[i] < menor:
        indice_menor = i

print("Tardo menos el metodo", i)