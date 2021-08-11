# Para obtener el total de ventas realizadas, una empresa comercial desea ingresar las facturas
# procesadas en el día. Las facturas pueden ser al contado, tipo (1), o a crédito, tipo (2), y se
# desean totales separados para cada tipo. No se conoce el total de facturas, y por ello, el
# proceso deberá concluir cuando se ingrese una factura de tipo (0). Escribir un algoritmo para
# realizar esta función.

while True:
  tipo_factura = int(input("""Ingrese el tipo de la factura:
(1) si la factura es contado
(2) si la factura es a credito
(0) para terminar el programa
"""))
  if (tipo_factura == 1):
    print('--El tipo de factura es contado--'.upper())
  elif (tipo_factura == 2):
    print('--El tipo de la factura credito--'.upper())
  else:
    break

print("--Programa finalizado--".upper())