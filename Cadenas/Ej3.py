cadena = input("Introduzca una cadena S1: ").upper()
cadena_disponibles = input("Introduzca una cadena S2: ").upper()

caracteres_usados = ""

cambiable = True
for caracter in cadena:
  if caracter not in cadena_disponibles:
     cambiable = False
  else:
    caracteres_usados += caracter

if cambiable and ((len(caracteres_usados) == len(cadena_disponibles)) or (caracteres_usados in caracteres_usados)):
  print("Si se puede escribir")
else:
  print("No se puede escribir")