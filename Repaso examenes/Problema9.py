fecha = input("Ingrese la fecha en formato: DD/MM/AAAA\n")
fechas = fecha.split("/")

numeros = [
    "uno",    "dos",     "tres",
    "cuatro", "cinco",   "Seis",
    "Siete",  "Ocho",    "Nueve",
    "diezi",  "once",    "doce",
    "trece",  "catorce", "quince",
]

decenas = [
    "",
    "diezi",  "veinti", "treinta", 
    "cuarenta y", "cincuenta y", "sesenta y", 
    "setenta y", "ocheanta y", "noventa y"
]

meses = [
    "enero",   "febrero",   "marzo",
    "abril",   "mayo",      "junio", 
    "julio",   "agosto",    "septiembre", 
    "octubre", "noviembre", "diciembre"
]

centenas = [""] + [0] * 7 + ["novescientos"]

anos = ["mil", "dos mil"]



def mostrar_dias(dia):
    mensaje = ""
    dia_int = int(dia)
    if dia_int < 10:
        mensaje = numeros[dia_int - 1]
    elif dia_int > 10 and dia_int < 16:
        mensaje = numeros[dia_int - 1]
    else:
        mensaje = decenas[int(dia[0])] +  numeros[int(dia[1]) - 1]

    return mensaje

def mostrar_meses(mes):
    return meses[int(mes) - 1]

def mostrar_ano(ano):
    return anos[int(ano[0]) - 1] + " " +  centenas[int(ano[1])] + " " + decenas[int(ano[2])] + " " + numeros[int(ano[3]) - 1]

print(mostrar_dias(fechas[0]), "de", mostrar_meses(fechas[1]), "de", mostrar_ano(fechas[2]))