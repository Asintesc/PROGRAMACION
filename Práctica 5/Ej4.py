print('Prática 5 Ej4')
print('Albert Sintes Coll')
n1 = int(input('Escribe un número: '))
factorial = 1
if n1 == 0:
    print('El factorial de ',n1,' es: 0')
else:
    for i in range (1,n1+1):
        factorial = factorial*i
print('El factorial de ',n1,' es: ',factorial)

