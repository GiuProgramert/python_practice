def main(n, p, alumnos, suma_calificaciones):  
  for i in range(0, n * 2, 2):
    for j in range(i + 2, n * 2, 2):
      if alumnos[j] < alumnos[i]:
        alumnos[i], alumnos[j] = alumnos[j], alumnos[i]
        alumnos[i + 1], alumnos[j + 1] = alumnos[j + 1], alumnos[i + 1]

  puntaje_separar = suma_calificaciones / p
  RES = []

  if p == 2:
    for i in range(n * 2 - 1):
      for j in range(i + 1, n * 2):
        if alumnos[i + 1] + alumnos[j + 1] == puntaje_separar:
            RES.append(alumnos[i])
            RES.append(alumnos[j])
  elif p == 3:
    for i in range(n * 2 - 2):
      for j in range(i + 1, n * 2 - 1):
        for z in range(j + 1, n * 2):
          if alumnos[i + 1] + alumnos[j + 1] + alumnos[z + 1] == puntaje_separar:
            RES.append(alumnos[i])
            RES.append(alumnos[j])
            RES.append(alumnos[z])
  elif p == 4:
    for i in range(n * 2 - 3):
      for j in range(i + 1, n * 2 - 2): 
        for z in range(j + 1, n * 2 - 1):
          for k in range(z + 1, n * 2):
            if alumnos[i + 1] + alumnos[j + 1] + alumnos[z + 1] + alumnos[k + 1] == puntaje_separar:
              RES.append(alumnos[i])
              RES.append(alumnos[j])
              RES.append(alumnos[z])
              RES.append(alumnos[k])
  elif p == 5:
    for i in range(n * 2 - 4):
      for j in range(i + 1, n * 2 - 3): 
        for z in range(j + 1, n * 2 - 2):
          for k in range(z + 1, n * 2 - 1):
            for x in range(k + 1, n * 2):
              if alumnos[i + 1] + alumnos[j + 1] + alumnos[z + 1] + alumnos[k + 1] + alumnos[x + 1] == puntaje_separar:
                RES.append(alumnos[i])
                RES.append(alumnos[j])
                RES.append(alumnos[z])
                RES.append(alumnos[k])
                RES.append(alumnos[x])

  j = 0
  for i in range(0, n * 2, p):
    j = j + 1
    print("El grupo", j)
    for j in range(0, p):
      print(RES[j])

alumnos= [1660, 49, 2007, 74, 2011, 47, 2466, 64, 2600, 75,  3089, 49, 3131, 96, 3460, 37, 3657, 84, 3719, 42, 4084, 77, 4215, 100, 4737, 62, 5264, 33]

main(15, 3, alumnos, 925)