numeros = []
n = int(input("Ingrese la cantidad de numeros: "))

for i in range(n):
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

valores = []
frecuencias = []

numeros.sort()

for numero in numeros:
    if numero not in valores:
        valores.append(numero)
        frecuencias.append(numeros.count(numero))        

print(numeros, valores, frecuencias)