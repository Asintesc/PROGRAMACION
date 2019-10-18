print ('Práctica5 Ej3')
print ('Albert Sintes Coll')

n1 = int(input('Escribe un número: '))
n2= int(input('Escribe otro número mayor: '))
if n2 < n1:
    print(n2,' no es mayor.')
else:
    for i in range (n1,n2+1):
        n3 = sum(range(n1,n2+1))
print()
print('La suma desde ',n1,' hasta',n2,' es: ',n3)

    
