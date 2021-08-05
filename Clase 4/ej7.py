precio = int(input('Introduzca el precio\n'))
categoria = int(input('Introduzca la categoria\n'))

descuento = 0
precio_final = 0
if categoria == 1:
  descuento = precio * 0.1
elif categoria == 2:
  descuento = precio * 0.15
elif categoria == 3:
  descuento = precio * 0.25
else:
  descuento = 0

if descuento == 0:
  descuento = "Descuento no valido porque no existe esa categoría"
  precio_final = precio
else:
  precio_final = precio - descuento
print(f'Descuento: {descuento} \nPrecio final: {precio_final}')  