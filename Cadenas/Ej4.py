cadena = input("Introduzca una cadena S1: ").lower()
cadena_disponibles = input("Introduzca una cadena S2: ").lower()

contador = 0
for caracter in cadena:
  if caracter in cadena_disponibles:
      contador += 1

if contador == len(cadena_disponibles):
  print("Se puede escribir")
else:
  print("No se puede escribir")