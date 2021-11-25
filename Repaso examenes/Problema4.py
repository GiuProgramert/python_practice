from random import random

bandera = True
while bandera == True:
    A = int(9 * random()) + 1
    B = int(9 * random()) + 1
    C = int(9 * random()) + 1
    D = int(9 * random()) + 1
    E = int(9 * random()) + 1

    if B ** 3 + 4 * D + E ** 2 == A * E + 5 * C ** (4 / 3):
        print(A, B, C, D, E)

