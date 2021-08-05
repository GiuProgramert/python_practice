from os import system

system("cls")

n = int(input('Ingrese al cantidad de empleados\n'))
precio_hora = int(input(f'Introduzca la paga por hora trabajada\n'))

paga_total = 0

for i in range(n):
  horas_trabajadas = int(input(f'Introduzca las horas trabajadas por el empleado {i + 1}\n'))
  if horas_trabajadas <= 40:
    paga = horas_trabajadas * precio_hora
  else:
    horas_extra = horas_trabajadas - 40
    paga = ((horas_trabajadas - horas_extra) * precio_hora) + (horas_extra * (precio_hora * 2))
  print('Se le pagaran: ', paga)
  paga_total += paga

billetes_a_calcular = 0
billetes_100 = 0
billetes_50 = 0
billetes_20 = 0
billetes_10 = 0
billetes_5 = 0
billetes_2 = 0
billetes_1 = 0

while billetes_a_calcular != paga_total or billetes_a_calcular > paga_total:
  diferencia = paga_total - billetes_a_calcular
  if diferencia >= 100000:
    billetes_a_calcular += 100000
    billetes_100 += 1
  elif diferencia >= 50000 and diferencia <= 100000:
    billetes_a_calcular += 50000
    billetes_50 += 1
  elif diferencia >= 20000 and diferencia <= 50000:
    billetes_a_calcular += 20000
    billetes_20 += 1
  elif diferencia <= 10000 and diferencia <= 20000:
    billetes_a_calcular += 10000
    billetes_10 += 1
  elif diferencia <= 5000 and diferencia <= 10000:
    billetes_a_calcular += 5000
    billetes_5 += 1
  elif diferencia <= 2000 and diferencia <= 5000:
    billetes_a_calcular += 2000
    billetes_2 += 1
  elif diferencia <= 1000 and diferencia <= 2000:
    billetes_a_calcular += 1000
    billetes_1 += 1

print('La paga total de todos los empleados es: ', paga_total)
print('Los billetes necesarios seran: ')
print(f'''
billetes de 100.000 = {billetes_100}
billetes de 50.000 = {billetes_50}
billetes de 20.000 = {billetes_20}
billetes de 10.000 = {billetes_10}
billetes de 5.000 = {billetes_5}
billetes de 2.000 = {billetes_2}
billetes de 1.000 = {billetes_1}
''')