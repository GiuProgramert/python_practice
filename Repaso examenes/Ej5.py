print("Calcular la moda y la mediana de una lista de N números")

numeros = []
n = int(input("Ingrese la cantidad de elementos: "))

for i in range(n):
    numeros.append(int(input("Ingrese el número: ")))

moda = 0
for i in range(n):
    if numeros.count(numeros[i]) > numeros.count(moda):
        moda = numeros[i]

numeros.sort()
if n % 2 == 0:
    mediana = numeros[n / 2] + numeros[(n / 2) + 1]
else:
    mediana = numeros[int(n / 2)]

print("La mosa es: ", moda)
print("La mediana es: ", mediana)