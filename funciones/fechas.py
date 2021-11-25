def bisiesto(ano):
  if ano % 100 == 0 and ano % 400 == 0:
    return True
  elif ano % 4 == 0:
    return True
  else:
    return False 

def contador_dias_anos(ano):
  contador = 0
  for i in range(1980, ano):
    contador += 365
    if bisiesto(i):
      contador += 1
  return contador

def contador_dias_meses(mes, ano):
  dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  contador = 0
  for i in range(mes - 1):
    contador += dias_mes[i]
  
  if bisiesto(ano) and mes >= 2:
    contador += 1
  return contador

#Contar lo días del ano del mes y como ultimo los días
def dias(f):
  return int(f[0]) + contador_dias_meses(int(f[1]), int(f[2])) + contador_dias_anos(int(f[2])) - 1

def fecha(d):
  dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  ano_actual = 1980
  mes_actual = 0
  dia_actual = 1
  dias_total = 0
  for i in range(d, 0, -1):
    dia_actual += 1
    if bisiesto(ano_actual):
      dias_mes[1] = 29
    else:
      dias_mes[1] = 28
    if dia_actual == dias_mes[mes_actual]:
      if mes_actual == 11:
        ano_actual += 1
        dia_actual = 1
        mes_actual = 0
      else:
        mes_actual += 1
        dia_actual = 1
  if mes_actual + 1 < 10:
    mes_actual = "0" + str(mes_actual + 1)
  if dia_actual + 1 < 10:
    dia_actual = "0" + str(dia_actual + 1)
  return f"{dia_actual}/{mes_actual}/{ano_actual}" 

d = int(input("Ingrese la cantidad de dias: "))
print(fecha(d))