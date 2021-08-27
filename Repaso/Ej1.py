n = int(input("Introduzca la cantidad de N: "))
lista = []

for i in range(n):
  cifra1 = int(input("Introduzca la primera cifra del número: "))
  cifra2 = int(input("Introduzca la segunda cifra del número: "))
  cifra3 = int(input("Introduzca la tercera cifra del número: "))
  lista.append(cifra1)
  lista.append(cifra2)
  lista.append(cifra3)

print("La lista original es: ", lista)

cambio = True
j = 0
while cambio:
  cambio = False
  j += 1
  for i in range(0, (n*3)-j-3, 3):
    num1 = lista[i] * 100 + lista[i + 1] * 10 + lista[i + 2]
    num2 = lista[i + 3] * 100 + lista[i + 4] * 10 + lista[i + 5]
    if num2 < num1:
      lista[i + 3], lista[i] = lista[i], lista[i + 3]
      lista[i + 4], lista[i + 1] = lista[i + 1], lista[i + 4]
      lista[i + 5], lista[i + 2] = lista[i + 2], lista[i + 5]
      cambio = True

print("La lista ordenada es: ", lista)