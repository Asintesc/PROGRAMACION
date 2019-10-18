n1 = int(input('Escribe un número: '))
n2 = int(input('Escribe otro número :'))
n3 = int(input('Escribe otro número: '))
n4 = int(input('Escribe el divisor: '))
if n1 % n4 == 0 and n2 % n4 == 0 and n3 % n4 == 0:
    print (n4,'es divisor de ',n1,',',n2,' y ',n3)
else:
    print (n4,'no es divisor de ',n1,',',n2,' y ',n3)
