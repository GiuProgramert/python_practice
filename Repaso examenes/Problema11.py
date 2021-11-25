from random import random
from time import time

def calcular_factorial(n):
    producto = 1
    for i in range(1, n + 1):
        producto = producto * i
    
    return producto

def palabra_a_lista(palabra):

    lista = []
    for caracter in palabra:
        lista.append(caracter)

    return lista

def generar_posibilidad(palabra):
    posibilidad = ""
    copia_palabra = palabra.copy()
    while len(copia_palabra) > 0:
        posicion = int(len(copia_palabra) * random())
        posibilidad = posibilidad + copia_palabra[posicion]
        copia_palabra.remove(copia_palabra[posicion])

    return posibilidad
        

palabra = palabra_a_lista(input("Ingrese la palabra que desea saber la cantidad de combinaciones que posee: "))

n = calcular_factorial(len(palabra))
posibilidades = []

i = 0
while i < n:
    posibilidad = generar_posibilidad(palabra)

    if posibilidad not in posibilidades:
        posibilidades.append(posibilidad)
        i = i + 1    

print(posibilidades)