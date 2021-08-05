print('Debe introducir 2 números de 3 digitos')

a1 = int(input('Introduzca el primer digito del número 1\n'))
a2 = int(input('Introduzca el segundo digito del número 1\n'))
a3 = int(input('Introduzca el tercer digito del número 1\n'))
print(f'El número 1 es {a1}{a2}{a3}')

b1 = int(input('Introduzca el primer digito del número 2\n'))
b2 = int(input('Introduzca el segundo digito del número 2\n'))
b3 = int(input('Introduzca el tercer digito del número 2\n'))
print(f'El número 2 es {b1}{b2}{b3}')

if (a1 + a2 + a3) == (b1 + b2 + b3):
  print('sus digitos suman lo mismo')
else:
  print('Sus dígitos no suman lo mismo')