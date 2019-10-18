objeto = str(input('Triángulo(T) o cuadrado(C): '))
b = float(input('Inserta la base del triángulo: '))
a = float(input('Inserta la altura del triángulo: '))
if objeto == 'T':
    area = (b*a)/2
    print ('El área del triángulo es: ',area)
elif objeto == 'C':
    area = b*a
    print ('El área del triángulo es: ',area)
else:
    print ('Objeto no válido.')
