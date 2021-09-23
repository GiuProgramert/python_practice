# En el juego conocido como “Generala” se utilizan cinco dados que se lanzan simultáneamente. De acuerdo a los valores obtenidos
# en esos dados se tienen las combinaciones ganadoras que se muestran a continuación. Escribir un algoritmo para preparar la tabla
# de frecuencias de estas combinaciones, a partir de N lanzamientos de los cinco dados.
# • Generala: cuando los cinco dados tienen igual valor.
# • Poker: cuando cuatro dados tienen igual valor y el quinto es diferente.
# • Foul: cuando tres dados tienen el mismo valor y los otros dos son iguales a otro valor. Ejemplos: 3,1,3,3,1 o 6,4,4,6,4
# • Escalera: Cuando los valores de los cinco dados forman una secuencia ascendente. Ejemplos: 1,3,2,5,4 o 5,4,2,6,3
from random import random

n = int(input("Ingrese la cantidad de veces que se lanzara la moneda: "))
frecuencias = [0, 0, 0, 0]

for i in range(n):
  #Generan los dados
  dados = []
  for j in range(5):
    dados.append(int(6 * random()) + 1)

  #Ordenar nos dados
  for j in range(4):
    for k in range(j + 1, 5):
      if dados[k] < dados[j]:
        dados[k],dados[j] = dados[j], dados[k]

  #Contar cantidad de iguales
  iguales = 0
  # cambio_distintos = 0
  for j in range(4):
    if dados[j] == dados[j + 1]:
      iguales += 1
    # else:
    #   cambio_distintos += 1

        
  #Verificar si es generala
  if iguales == 4:
    frecuencias[0] = frecuencias[0] + 1
#--------------------------------------------------------------------
  #verificar poker o foul
  elif iguales == 3:
    #Contar la cantidad de veces que se repite un número
    cantidad_repeticiones = [0, 0, 0, 0, 0, 0]
    for j in range(5):
      cantidad_repeticiones[dados[j] - 1] = cantidad_repeticiones[dados[j] - 1] + 1 
    
    #Calcula la diferencia entre la cantidad del número
    diferencia = 0
    for j in range(6):
      if cantidad_repeticiones[j] != 0:
        if diferencia == 0:
          diferencia = cantidad_repeticiones[j]
        else:
          diferencia = diferencia - cantidad_repeticiones[j]
    
    #Si la diferencia es |3| es poker y si |1| es foul 
    if diferencia == 3 or diferencia == -3:
      frecuencias[1] = frecuencias[1] + 1
    elif diferencia == 1 or diferencia == -1:
      frecuencias[2] = frecuencias[2] + 1
#--------------------------------------------------------------------
  #verficar si es escalera
  else:
    es_escalera = True
    for j in range(4):
      if dados[j] + 1 != dados[j + 1]:
        es_escalera = False
      
    if es_escalera:
      frecuencias[3] = frecuencias[3] + 1

print(f"""
Cantidades:
Generala: {frecuencias[0]}
Poker: {frecuencias[1]}
Foul: {frecuencias[2]}
Escalera: {frecuencias[3]} 
""")
  