print('Realizar operaciones con los triangulos segun su tipo:\n')

lado_a = float(input('Introduzca el lado A del triangulo\n'))
lado_b = float(input('Introduzca el lado B del triangulo\n'))
lado_c = float(input('Introduzca el lado C del triangulo\n'))

perimetro = lado_a + lado_b + lado_c
operacion = ""

if lado_a == lado_b == lado_c:
  altura = (3 ** (1 / 2) * lado_a) / 2
  area  = (altura * lado_a) / 2
  operacion = f"El perimetro es {perimetro} y area es: {area}"
elif lado_a != lado_b != lado_c:
  operacion = f"El perimetro es {perimetro}"
else:
  lado = 0
  base = 0
  if lado_a == lado_b:
    lado = lado_a
    base = lado_c
  elif lado_a == lado_c:
    lado = lado_a
    base = lado_b
  else:
    lado = lado_b
    base = lado_a

  altura = (((4 * lado ** 2) + (base ** 2)) ** (1 / 2)) / 2
  area = (altura * base) / 2
  operacion = f"El area es {area}"

print(operacion)