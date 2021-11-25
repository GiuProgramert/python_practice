resultados = []
n = 18

for i in range(n):
    equipo1 = int(input("Ingrese el equipo 1: "))
    puntos_equipo1 = int(input("Ingrese los puntos que hizo el equipo 1: "))
    equipo2 = int(input("Ingrese el equipo 2: "))
    puntos_equipo2 = int(input("Ingrese los puntos que hizo el equipo 2: "))

    resultados.append(equipo1)
    resultados.append(equipo2)
    resultados.append(puntos_equipo1)
    resultados.append(puntos_equipo2)

# [(1 , 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)]
# [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10)]
# [(3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10)]
# [(4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10)]
# [(5, 6), (5, 7), (5, 8), (5, 9), (5, 10)]
# [(6, 7), (6, 8), (6, 9), (6, 10)]
# [(7, 8), (7, 9), (7, 10)]
# [(8, 9), (8, 10)]
# [(9 ,10)]

equipo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
puntos = [0] * 10

for i in range(1, n, 4):
    if resultados[i + 2] > resultados[i + 3]:
        puntos[resultados[i] - 1] += 3
    elif resultados[i + 2] < resultados[i + 3]:
        puntos[resultados[i + 1] - 1] += 3
    else:
        puntos[resultados[i] - 1] += 1
        puntos[resultados[i + 1] - 1] += 1


print("Los puntos del equipo son: ", puntos)