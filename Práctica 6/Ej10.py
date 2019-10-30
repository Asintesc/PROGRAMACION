#Práctica 6 Ej10
#Alebrt Sintes Coll
nombre = ''
lista = []
while True:
    alumno_datos = []
    alumno = str(input('Dime el nombre del alumno: '))
    if alumno == '':
        break
    alumno_datos.append(alumno)
    nota = 1
    while (nota >= 0) and (nota <= 10):
        nota = int(input('Escribe una nota: '))
        if (nota > 10) or (nota < 0):
            break
        alumno_datos.append(nota)
    lista.append(alumno_datos)
print('Las notas de los alumnos son: ')
for i in (lista):
    final = ", ".join(map(str,i[1:]))
    print(i[0]+': '+final)


