#Práctica6 Ej1
#Albert Sintes Coll
lista = []
palabra = str(input('Escribe una palabra: '))
lista.append(palabra)
while palabra != '':
    palabra = str(input('Escribe otra palabra: '))
    lista.append(palabra)
print(lista[:-1])
