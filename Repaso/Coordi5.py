from random import randint

lista = []

for i in range(30):
    lista.append(randint(1, 10))

salto = int(30 / 2)
while salto >= 1:
    cambio = False
    i = 0
    while (i + salto) <= (30 - 1):
        if lista[i] > lista[i + salto]:
            lista[i], lista[i + salto] = lista[i + salto], lista[i]
            cambio = True
        i += 1
    if not cambio:
        salto = int(salto / 2)

contador_repeticiones = 0
elemento_mas_repetido = 1
posicion_mas_repetido = 1

for i in range(29):
	contador_repeticiones_aux = 0
	for j in range(i + 1, 30):
		if lista[i] == lista[j]:
			contador_repeticiones_aux += 1
		elif contador_repeticiones_aux > contador_repeticiones and lista[i] != lista[j]:
			contador_repeticiones = contador_repeticiones_aux
			elemento_mas_repetido = j - 1
			posicion_mas_repetido = i - 1

print(lista)
print("Elemento que más se repite de forma continua: ", elemento_mas_repetido)
print("La posición del elemento más repetido es: ", posicion_mas_repetido)