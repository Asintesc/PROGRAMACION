#Práctica 6 Ej 8
#Albert Sintes Coll
lista = []
limite = int(input('Escribe un límite: '))
suma = 0
n1 = 0
while suma != limite:
    if n1 != (0):
        n1 = int(input('Escribe otro valor: '))
    else:
        n1 = int(input('Escribe un valor: '))
    while (suma+n1) > limite:
        n1 = int(input('%s es demasiado grande, escribe otro número: ' %(n1)))
    if n1 != (0):
        lista.append(n1)
        suma += n1
print('El límite es ',limite,'.La lista es: ',','.join(map(str,lista)),' ya que la \n\
suma de los números es: ',sum(lista))

