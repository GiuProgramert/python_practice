def calcular_hipotenusa(a, b):
  hipotenusa = (a ** 2 + b ** 2) ** (1 / 2)
  return hipotenusa

def calcular_perimetro(a, b):
  hipotenusa = calcular_hipotenusa(a, b)
  perimetro = hipotenusa + a + b
  return perimetro

print(calcular_perimetro(3, 4))