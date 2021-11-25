print("Ordenar alfabeticamente un alfa númerico")

texto = input("Introduzca el texto: ")
n = len(texto) - 1

salto = int(n / 2)
while salto >= 1:
  cambio = False
  i = 0
  while (i + salto) <= (n):
    if texto[i + salto] < texto[i]:
      
      anterior = texto[0:i:1] # lo que esta antes de i
      medio = texto[(i + 1):(i + salto):1] # lo que esta entre i e y
      final = texto[(i + salto + 1):(n + 1):1] # lo que esta despues de y

      #Estructura inicial antes del cambio
      # anterior + texto[i] + medio + texto[i + salto] + final

      #Extructura final al cambiar i entre i + salto
      texto = anterior + texto[i + salto] + medio + texto[i] + final

      cambio = True
    i += 1
  
  if not cambio: 
    salto = int(salto / 2)

print(texto)