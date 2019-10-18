print('Práctica 5 Ej9')
print('Albert Sintes Coll')
n1 = int(input('Anchura del rectágulo: '))
n2 = int(input('Altura del rectángulo: '))
for i in range(n2):
    for j in range(n1):
        if i in [0, n2-1] or j in[0, n1-1]:
            print('*',end='')
        else:
            print(' ',end='')
    print()
