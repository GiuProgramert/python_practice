print('Hallar las raices reales de Ax^2 + Bx + C = 0')

def pedir_datos():
  A = float(input('Debe ingresar el valor de A\n'))
  B = float(input('Debe ingresar el valor de B\n'))
  C = float(input('Debe ingresar el valor de C\n'))
  return A, B, C

def continuar_programa():
  desicion = input('Desea resolver otra ecuación [si/s] para continuar o [no/n] para terminar\n').lower()
  while (desicion != "si") and (desicion != "s") and (desicion != "no") and (desicion != "n"):
    desicion = input('Desea resolver otra ecuación [si/s] para continuar o [no/n] para terminar\n').lower()
  if desicion.startswith('s'):
    return True
  else:
    return False

def comprobar_raiz_real(A, B, C, raiz):
  if raiz < 0:
    print('Las raices no son enteras')
    continuar_programa()
    A, B, C = pedir_datos()
    raiz = B ** 2 - 4 * A * C
  return A, B, C

def obtener_raices(A, B, raiz):
  x1 = (B + raiz) / (2 * A)
  x2 = (B - raiz) / (2 * A)
  return x1, x2

def main():
  A, B, C = pedir_datos()
  raiz = B ** 2 - 4 * A * C
  A, B, C = comprobar_raiz_real(A, B, C, raiz)
  x1, x2 = obtener_raices(A, B, raiz)
  print(f"Las raices son x1 = {x1} y x2 = {x2}")

if __name__ == '__main__':
  while True:
    main()
    if not(continuar_programa()):
      break
  print('Programa terminado')