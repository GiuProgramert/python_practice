palabra = input("Ingrese la palabra a ser códificada: ")

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_codigo = "bcdebcdefghijklmnñopqrstuvwxyza"

palabra_codigo = str()

for caracter in palabra:
  posicion = alfabeto.find(caracter)
  if posicion >= 0:
    palabra_codigo = palabra_codigo + alfabeto_codigo[posicion]
  else:
    palabra_codigo = palabra_codigo + caracter

print("La palabra código es: ", palabra_codigo)