from random import random

jugadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in range(10):
    n = int(len(jugadores) * random()) + 1
    jugadores.remove(jugadores[n - 1])

print("El jugador que va a contar es: ", jugadores[0])
