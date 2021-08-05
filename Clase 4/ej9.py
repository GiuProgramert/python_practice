año = int(input('introduzca el año\n'))

if ((año % 100) == 0) and ((año % 400) == 0):
  print('Es un año bisiesto')
elif ((año % 4) == 0):
  print('Es un año bisiesto')
else:
  print('No es un año bisiesto')