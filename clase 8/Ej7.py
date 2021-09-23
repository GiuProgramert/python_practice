# En realidad, las reglas del juego “Generala” permiten que jugador realice hasta un máximo de tres lanzamientos de 
# los dados para buscar alguna de las combinaciones ganadoras. En la primera oportunidad, el jugador debe lanzar 
# los cinco dados. Para la segunda oportunidad, el jugador puede conservar algunos de los dados lanzados y lanzar solo 
# los restantes. En la tercera oportunidad, si aún no ha obtenido una combinación ganadora, puede proceder como en la 
# segunda oportunidad. Escribir un algoritmo que permita realizar hasta tres lanzamientos siguiendo las reglas de este juego 
# y que detecte cuando aparece una combinación ganadora, imprimiendo su nombre.
from random import random

n = int(input("Ingrese la cantidad de veces que se lanzaran los dados: "))

for i in range(n):
  dados = []
  for j in range(5):
    dados.append(int(6 * random()) + 1)

  print("Sus dados son: ", dados)
  dados_copia = [
    dados[0], dados[1], dados[2], dados[3], dados[4]
  ]
  c = 0
  cambiar = True
  while cambiar == True:
    cambiar = False
    desicion = input("Desea cambiar alguno [S] para sí y [N] para no: ")
    if desicion == "S" and c < 3:
      dado_cambiar = int(input("Introduzca la posición del dado que desea cambiar [1 - 5]: "))
      dados_copia[dado_cambiar - 1] = int(6 * random()) + 1
      c = c + 1
      cambiar = True
    print(dados_copia)
    
    dados = [
    dados_copia[0], dados_copia[1], dados_copia[2], dados_copia[3], dados_copia[4]
    ]
    for j in range(4):
      for k in range(j + 1, 5):
        if dados[k] < dados[j]:
          dados[k],dados[j] = dados[j], dados[k]
  
    iguales = 0
    for j in range(4):
      if dados[j] == dados[j + 1]:
        iguales += 1
          
    if iguales == 4:
      print("Es generala")
    elif iguales == 3:
      cantidad_repeticiones = [0, 0, 0, 0, 0, 0]
      for j in range(5):
        cantidad_repeticiones[dados[j] - 1] = cantidad_repeticiones[dados[j] - 1] + 1 
      
      diferencia = 0
      for j in range(6):
        if cantidad_repeticiones[j] != 0:
          if diferencia == 0:
            diferencia = cantidad_repeticiones[j]
          else:
            diferencia = diferencia - cantidad_repeticiones[j]
      
      if diferencia == 3 or diferencia == -3:
        print("Es poker")
      elif diferencia == 1 or diferencia == -1:
        print("Es four")
    else:
      es_escalera = True
      for j in range(4):
        if dados[j] + 1 != dados[j + 1]:
          es_escalera = False
        
      if es_escalera:
        print("Es escalera")
  print("Ya no puedes realizar ningun cambio")