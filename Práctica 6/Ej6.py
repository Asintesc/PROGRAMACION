#Práctica 6 Ej6
#Albert Sintes Coll
lista = []
n1 = int(input('Escribe un número: '))
lista.append(n1)
n2 = int(input('Escribe un número mayor que %d: ' %(n1)))
lista.append(n2)
while n2 < n1:
    n2 = int(input('%d no es mayor, escribe un número mayor que %d: ' %(n2,n1)))
    lista.append(n2)
n3 = int(input('Escribe un número entre %d y %d: ' %(n1,n2)))
lista.append(n3)
while n3 > n1 and n3 < n2:
    n3 = int(input('Escribe un número entre %d y %d: ' %(n1,n2)))
    lista.append(n3)
print('Los números entre %d y %d que has escrito son: '%(n1,n2),','.join(map(str,lista[2:-1])))
