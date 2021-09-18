print("Horario de llegada")

introducir = True
n = 0
ES = []
while introducir == True:
  numero_empleado = int(input("Introduzca su número de empleado: "))
  horas_trabajadas = int(input("Introduzca las horas trabajadas: "))
  minutos_trabajados = int(input("Introduzca los minutos trabajados: "))
  ES.append(numero_empleado)
  ES.append(horas_trabajadas)
  ES.append(minutos_trabajados)
  n = n + 1

  opcion = int(input("si ya no desea agregar registros introduzca 0 y 1 para continuar: "))
  if opcion == 0:
    introducir = False

#Horario de salida y de retirada juntos
ES_aux = []
#Longitud del horario de salidad
ES_aux_lon = 0
for i in range(0, n * 3, 3):
  #Verificar que estamos interando primero el horario de entrada
  existe_ES_AUX = False
  for z in range(0, ES_aux_lon, 2):
    if ES[i] == ES_aux[z]:
      existe_ES_AUX = True
  
  #Si es el horario de entrada se ejecuta
  if existe_ES_AUX == False:
    salida_encontrada = False
    j = i + 3
    #Carga en ES_aux el número de trabajador, horario de salida - horario de entrada
    while salida_encontrada == False:
      if ES[i] == ES[j]:
        salida_encontrada = True

        #Pasar a minutos
        horario_entrada = ES[i + 1] * 60 + ES[i + 2] 
        horario_salida = ES[j + 1] * 60 + ES[j + 2] 
        
        ES_aux.append(ES[i])
        ES_aux.append(horario_salida - horario_entrada)
        ES_aux_lon = ES_aux_lon + 2
      else:
        j = j + 3

for i in range(0, ES_aux_lon, 2):
  horas = int(ES_aux[i + 1] / 60)
  minutos = int((ES_aux[i + 1] / 60 - horas) * 60)
  print("El empleado", ES_aux[i], "permanecio en la empresa", horas, "horas y", minutos, "minutos")