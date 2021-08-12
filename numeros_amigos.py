print("Ver si 2 números son amigos")
numero1 = int(input("Introduzca el número 1: "))
numero2 = int(input("Introduzca el número 2: "))

suma_divisores_1 = 0
suma_divisores_2 = 0

for i in range (1, numero1):
    if numero1 % i == 0:
        suma_divisores_1 += i
        
for i in range (1, numero2):
    if numero2 % i == 0:
        suma_divisores_2 += i

if suma_divisores_1 == numero2 and suma_divisores_2 == numero1:
    print("Son números amigos")
else:
    print("No son números amigos")