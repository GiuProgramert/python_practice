
n = int(input("Ingrese la cantidad N de la lista: "))
lista = []
for i in range(n):
  elemento = float(input("Ingrese un elemento de la lista: "))
  lista.append(elemento)

#* 07:00 -> 07:59 | 08:00 -> 08:59 | 09:00 -> 09:59 | 10:00 -> 10:59 | 
#* 11:00 -> 11:59 | 12:00 -> 12:59 | 13:00 -> 13:59 | 14:00 -> 14:59 | 
#* 15:00 -> 15:59 | 16:00 -> 16:59 | 17:00 -> 17:59 | 18:00 -> 18:59 |

CONTADOR_HORARIOS = [
  0, 0, 0, 0,
  0, 0, 0, 0,
  0, 0, 0, 0
]
HORARIOS = [
  7.0, 8.0, 9.0, 10.0, 
  11.0, 12.0, 13.0, 14.0, 
  15.0, 16.0, 17.0, 18.0, 
]
LON_HORARIOS = 12

for i in range(0, int(n / 2), 2):
  for j in range(LON_HORARIOS):
    #Puede poner el horario a excepción del ultimo horario que no lo aumenta
    minutos2 = int(int(lista[i + 1]) * 60 + (lista[i + 1] - int(lista[i + 1])) * 60)
    horarios2 = int(HORARIOS[j] * 60 + 59)
    if minutos2 > horarios2:
      CONTADOR_HORARIOS[j] = CONTADOR_HORARIOS[j] + 1

for i in range(LON_HORARIOS - 1):
  for j in range(i + 1, LON_HORARIOS):
    if CONTADOR_HORARIOS[j] > CONTADOR_HORARIOS[i]:
      CONTADOR_HORARIOS[i], CONTADOR_HORARIOS[j] = CONTADOR_HORARIOS[j], CONTADOR_HORARIOS[i]
      HORARIOS[i], HORARIOS[j] = HORARIOS[j] , HORARIOS[i]

z = []
for i in range(LON_HORARIOS):
  hora_entrada = HORARIOS[i]
  hora_salida_minuto = HORARIOS[i] + 0.98
  hora_salida = int(hora_salida_minuto)
  minuto_salida = int((hora_salida_minuto - hora_salida) * 60 + 1)

  z.append(int(hora_entrada))
  z.append(hora_salida)
  z.append(minuto_salida)
  z.append(CONTADOR_HORARIOS[i])


for i in range(0, LON_HORARIOS * 4, 4):
  print("Horario", z[i], ": 00 - ", z[i + 1], ":", z[i + 2], "Presentes", z[i + 3])