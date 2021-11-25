meses = [
    31, 28, 31, 30,
    31, 30, 31, 31,
    30, 31, 30, 31
]

def fecha_a_dias(fechas):
    dias_meses = 0
    for i in range(int(fechas[1])):
        dias_meses = dias_meses + meses[i]
    
    return int(fechas[0]) + dias_meses

def dias_a_fecha(dias, agno):
    dias_meses = 0

    i = 0
    while dias > 28:
        dias_meses = dias_meses + 1
        dias = dias - meses[i]
        i = i + 1
    
    return str(dias) + "/" + str(dias_meses) + "/" + str(agno)

fecha1 = input("Ingrese la primera fecha: ").split("/")
fecha2 = input("Ingrese la segunda fecha: ").split("/")

fecha1_dias = fecha_a_dias(fecha1)
fecha2_dias = fecha_a_dias(fecha2)

agno = fecha1[2]

fecha_medio_dias = 0 

if fecha1_dias > fecha2_dias:
    fecha_medio_dias = int((fecha1_dias - fecha2_dias) / 2) + fecha2_dias
else:
    fecha_medio_dias = int((fecha2_dias - fecha1_dias) / 2) + fecha1_dias

fecha_medio = dias_a_fecha(fecha_medio_dias, agno)

print(fecha_medio)