#Práctica 6 Ej2
#Albert Sintes Coll
lista = []
numero = str(input('Escribe un número: '))
numero = numero.lower()
lista.append(numero)
while numero != 'salir':
    numero = str(input('Escribe otro número: '))
    numero = numero.lower()
    lista.append(numero)
print(lista[:-1])
