texto = input("Introduzca un texto: ").lower()

consonantes = "bcdfghjklmnñpqrstvwxyz"

cantidad_consonantes = 0

for caracter in texto:
  if caracter in consonantes:
    cantidad_consonantes += 1

print("La cantidad de consonates es:", cantidad_consonantes)