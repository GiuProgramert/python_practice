numero = int(input('Introduzca un número\n'))

if (numero % 4) == 0:
  print(numero ** (1 / 3))
elif (numero % 2) != 0:
  print(numero * 2)
else:
  print(10 / numero)