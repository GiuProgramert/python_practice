print("Contar e imprimir las palabras que existen en un texto: ")

texto = input("Introduzca el texto: ").lower() + "."
ABC = "aábcdeéfghiíjklmnoóñpqrstuúüvwxyz"

palabra = ""
cantidad_palabras = 0
for caracter in texto:
  if caracter in ABC:
    palabra += caracter
  elif len(palabra) != 0:
    cantidad_palabras += 1
    print(palabra)
    palabra = ""

print("La candidad de palabras es: ", cantidad_palabras)