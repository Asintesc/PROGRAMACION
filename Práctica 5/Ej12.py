print('Práctica5 Ej12')
print('Albert Sintes Coll')
n1 = int(input('Escribe un número: '))
cont = 0
for i in range (1,n1+1):
    if n1 % i == 0:
        cont = cont+1
if cont == 2:
    print(n1,'es primo.')
else:
    print(n1,'no es primo.')
