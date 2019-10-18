n1 = int(input('Escribe un número: '))
n2 = int(input('Escribe otro número: '))
n3 = int(input('Escribe otro número: '))
n4 = int(input('Escribe otro número: '))
n5 = int(input('Escribe otro número: '))

if n1 > n2 > n3 > n4 > n5:
    print ('Decreciente.')
elif n1 < n2 < n3 < n4 < n5:
    print ('Creciente.')
else:
    print ('Desordenado.')
