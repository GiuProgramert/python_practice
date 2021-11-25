palabra = input("Ingrese la palabra a ser códificada: ").lower()
desplazamiento = int(input("Introduza cuantas letras se va a dezplazar el alfabeto: "))

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
resto = desplazamiento % len(alfabeto)
alfabeto_codigo = ""

antes = alfabeto[0:resto:1] # antes del resto
despues = alfabeto[resto:len(alfabeto):1] # despues del resto
alfabeto_codigo = despues + antes

palabra_codigo = ""

for caracter in palabra:
  posicion = alfabeto.find(caracter)
  if posicion >= 0:
    palabra_codigo = palabra_codigo + alfabeto_codigo[posicion]
  else:
    palabra_codigo = palabra_codigo + caracter

print("La palabra código es: ", palabra_codigo)