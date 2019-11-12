diccionari = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
    }
fecha = input("Dime la fecha: ")
def fecha_mes(d,f):
    split = f.split("/")
    mes = int(split[1])
    print(split[0],'de',d[mes],'de',split[2])
    return mes
fecha_mes(diccionari, fecha)

