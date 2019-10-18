print('Práctica5 Ej8')
print('Albert Sintes Coll')
n1 = int(input('Altura del triángulo: '))
for i in range(n1+1):
    print('*'*i)
    print()
for j in range(n1,0,-1):
    for k in range(0,j-1,1):
        print('*', end= '')
    print('')
    print()

