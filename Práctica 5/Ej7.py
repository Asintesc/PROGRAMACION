print('Práctica 5 Ej7')
print('Albert Sintes Coll')
n1 = int(input('Altura del triángulo: '))
for i in range(n1,0,-1):
    for j in range(0,i,1):
        print('*', end=' ')
    print('')
