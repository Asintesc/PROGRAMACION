#Práctica 6 Ej 9
#Albert Sintes Coll
lista = []
nombre = str(input('Dame un nombre: '))
tel = str(input('Dame el teléfono: '))
nombre = nombre.lower()
lista.append([nombre,tel])
while nombre != 's':
    nombre = str(input('Dame un nombre: '))
    tel = str(input('Dame un teléfono: '))
    nombre  = nombre.lower()
    lista.append([nombre,tel])
print('Los números y teléfonos de la agenda son: ')
for i in (lista[:-1]):
    print(*i, sep=' : ')
