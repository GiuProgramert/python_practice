horas_trabajadas = int(input('Introduzca las horas trabajadas\n'))
precio_hora = int(input('Introduzca la paga por hora trabajada\n'))

if horas_trabajadas <= 40:
  paga = horas_trabajadas * precio_hora
else:
  horas_extra = horas_trabajadas - 40
  paga = ((horas_trabajadas - horas_extra) * precio_hora) + (horas_extra * (precio_hora * 2))

print('Se le pagaran: ', paga)