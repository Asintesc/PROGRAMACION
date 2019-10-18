print('Práctica 5 Ej11')
print('Albert Sintes Coll')
n1 = int(input('Escribe un número: '))
print('Los divisores de ',n1,' son: ')
for i in range(1,n1+1):
    if n1 % i == 0:
        print(i,',',end='')
        
