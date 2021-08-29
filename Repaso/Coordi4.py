nro1 = int(input("Introduzca el número 1: "))
nro2 = int(input("Introduzca el número 2: "))

#Nro1 * Nro2
suma_multiplicacion = 0
for i in range(nro2):
  suma_multiplicacion = suma_multiplicacion + nro1

print(suma_multiplicacion)
#Nro1 ** Nro2
suma_potencia = 0
for i in range(nro2):
  for j in range(nro1):
    suma_potencia += nro1
print(suma_potencia)
# 5.5