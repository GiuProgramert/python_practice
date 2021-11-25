print("Calcular la moda y la mediana de una lista de N números")

numeros = []
n = int(input("Ingrese la cantidad de elementos: "))
g = int(input("Ingrese el numero que debemos buscar: "))

for i in range(n):
    numeros.append(int(input("Ingrese el número: ")))

posiciones = []
for i in range(n - 1):
    for j in range(i + 1, n):
        suma = numeros[i] + numeros[j]
        if suma < g:
            if g - suma in numeros:
                k = numeros.index(g - suma)
                if i not in posiciones and j not in posiciones and k not in posiciones: 
                    posiciones.append(i)
                    posiciones.append(j)
                    posiciones.append(k)
    
    if len(posiciones) > 0:
        break

print("las posiciones son: ", posiciones)