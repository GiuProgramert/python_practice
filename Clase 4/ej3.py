print('Debe introducir un números de 3 digitos')

digito_1 = int(input('Introduzca el primer digito del número\n'))
digito_2 = int(input('Introduzca el segundo digito del número\n'))
digito_3 = int(input('Introduzca el tercer digito del número\n'))

mayor = 0
if (digito_1 > digito_2) and (digito_1 > digito_3):
  mayor = digito_1
elif (digito_2 > digito_1) and (digito_2 > digito_3):
  mayor = digito_2
else:
  mayor = digito_3

print(f'El digito mayor es {mayor}')