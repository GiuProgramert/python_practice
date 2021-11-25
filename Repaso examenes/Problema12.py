texto = "Espero la respuesta (a la nota (de hoy) sobre el PROBLEMA) lo antes posible. Debe quedar: Espero la respuesta lo antes posible."

texto_formateado = ""
if texto.count("(") == 1:
    texto_formateado = texto[0:texto.index("("):1] + texto[texto.index(")") + 2:len(texto):1]
else:
    #Agarrar todo desde el primer parentesis que se habra hasta el primero que se cierre 
    #Solo que no sacamos el primer parentesis que se cierra y lo usamos para 
    #Substraer desde el parentesis que se cierra mencionado anteriormene y sacamos de la 
    #posicion siguiente a la que esta hasta el ultimo parentesis que se cierre
    primer_parentesis_cerrado = texto.index(")")
    texto_formateado = texto[0:texto.index("("):1] + texto[texto.index(")"):len(texto):1]
    texto_formateado = texto_formateado[0:texto_formateado.index(")"):1] + texto_formateado[texto_formateado.index(")", texto_formateado.index(")") + 1) + 2:len(texto_formateado):1]

print(texto_formateado)