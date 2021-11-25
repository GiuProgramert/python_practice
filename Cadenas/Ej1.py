print("Conjugar un verbo terminado en 'ar' en el tiempo presente: ")

verbo = input("Introduzca el verbo: ").lower()

l_verbo = len(verbo)

if verbo[l_verbo - 2:] == "ar":
  print("Yo: ", verbo[:l_verbo - 2] + "o")
  print("Tu: ", verbo[:l_verbo - 1] + "s")
  print("El: ", verbo[:l_verbo - 1])
  print("Nosotros: ", verbo[:l_verbo - 1] + "mos")
  print("Vosotros: ", verbo[:l_verbo - 2] + "áis")
  print("Ellos: ", verbo[:l_verbo - 1] + "n")
elif verbo[l_verbo - 2:] == "er":
  print("Yo: ", verbo[:l_verbo - 2] + "o")
  print("Tu: ", verbo[:l_verbo - 1] + "s")
  print("El: ", verbo[:l_verbo - 1])
  print("Nosotros: ", verbo[:l_verbo - 1] + "mos")
  print("Vosotros: ", verbo[:l_verbo - 2] + "éis")
  print("Ellos: ", verbo[:l_verbo - 1] + "n")
elif verbo[l_verbo - 2:] == "ir":
  print("Yo: ", verbo[:l_verbo - 2] + "o")
  print("Tu: ", verbo[:l_verbo - 2] + "es")
  print("El: ", verbo[:l_verbo - 2] + "e")
  print("Nosotros: ", verbo[:l_verbo - 1] + "mos")
  print("Vosotros: ", verbo[:l_verbo - 2] + "ís")
  print("Ellos: ", verbo[:l_verbo - 2] + "en")