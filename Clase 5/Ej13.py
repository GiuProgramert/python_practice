# Se buscan dos números de tres cifras que cumplen con la siguiente condición:
# ABC * 2 = CAB – 151. Encontrar esos números sabiendo que A, B y C representan sus cifras.

for A in range(10):
  for B in range(10):
    for C in range(10):
      ABC = 100 * A + 10 * B + C
      CAB = 100 * C + 10 * A + B
      if ABC * 2 == CAB - 151:
        print(ABC)
        print(CAB)