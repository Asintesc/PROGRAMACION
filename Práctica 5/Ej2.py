print('Práctica 5 Ej2')
print('Albert Sintes Coll')
n1 = int(input('Escribe un número: '))
n2 = int(input('Escribe un número mayor: '))
if n2 < n1:
    print(n2,' no es mayor que ',n1)
else:
    for i in range (n1,n2):
        if (i % 2 == 0):
            print (i,' es par.')
        else:
            print(i,' es impar.')
    
