#Práctica6 Ej5
#Albert Sintes Coll
lista=[]
n1 = int(input('Esccribe un número: '))
lista.append(n1)
n2 = int(input('Escribe un número mayor que %d: '%(n1)))
lista.append(n2)
while n2 > n1:
    n1 = n2
    n2 = int(input('Escribe un número mayor que %d: '%(n1)))
    lista.append(n2)
print('Los números que has escrito son: ',','.join(map(str,lista[:-1])))

