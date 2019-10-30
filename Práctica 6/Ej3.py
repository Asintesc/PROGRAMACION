#Práctica 6 Ej3
#Albert Sintes Coll
lista = []
nota = float(input('Escribe una nota: '))
lista.append(nota)
while nota >= 0 and  nota <= 10:
    nota = float(input('Escribe otra nota: '))
    lista.append(nota)
print('Las notaas son: ',lista[:-1])
