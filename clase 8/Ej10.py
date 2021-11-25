from random import random

def generar_bolillas():
    bolillas = []
    i = 0
    while i < 5:
        bolilla = int(90 * random) + 1
        if bolilla not in bolillas:
            bolillas.append(bolilla)
            i += 1
    
    return bolillas

def ordenadas_ascendentemente(bolillas):
    es_ascendente = True
    for i in range(len(bolillas) - 1):
        if bolillas[i] > bolillas[i + 1]:
            es_ascendente = False

    return es_ascendente


n = int(input("Ingrese la cantidad de veces que se va simular el experimento: "))
contador_ascendentes = 0

for i in range(n):
    bolillas = generar_bolillas()
    if ordenadas_ascendentemente(bolillas):
        contador_ascendentes += 1

probabilidad = contador_ascendentes / n
print("La probabilidad es: ", probabilidad)