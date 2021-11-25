mesa1 = [10, 20, 30, 40, 50]
mesa2 = [60, 70, 80, 90, 100, 110]
mesa3 = [120, 130, 140, 150, 160, 170, 180]
mesa4 = [190, 200, 210, 220, 230, 240, 250, 260]

def registrar_votantes(mesa):
    votantes = []
    cambio = True
    print("Ingrese los votantes de la mesa:", mesa)
    while cambio == True:
        elemento = int(input("Ingrese el elemento ingresar -1 para terminar: "))
        votantes.append(elemento)

        if elemento == -1:
            cambio = False
    
    return votantes

def contar_votos(votantes):
    hay_duplicado = False
    for i in range(len(votantes)):
        if votantes.count(votantes[i]) > 1:
            hay_duplicado = True

    return hay_duplicado

votantes1 = registrar_votantes(1)
votantes2 = registrar_votantes(2)
votantes3 = registrar_votantes(3)
votantes4 = registrar_votantes(4)

if contar_votos(votantes1):
    print("En la mesa 1 esta duplicado el voto")
elif contar_votos(votantes2):
    print("En la mesa 2 esta duplicado el voto")
elif contar_votos(votantes3):
    print("En la mesa 3 esta duplicado el voto")
elif contar_votos(votantes4):
    print("En la mesa 4 esta duplicado el voto")