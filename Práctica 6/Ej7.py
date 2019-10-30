#Práctica 6 Ej 7
#Albert Sintes Coll
lista = []
limite = int(input('Escribe un límite: '))
n1 = int(input('Escribe un valor: '))
lista.append(n1)
suma = n1
while suma < limite:
    n1 = int(input('Escribe un valor: '))
    suma += n1
    lista.append(n1)
    sum(lista)
print('El límite es ',limite,' La lista es: ',','.join(map(str,lista)),' ya que la suma de los \
números es: ',sum(lista))
