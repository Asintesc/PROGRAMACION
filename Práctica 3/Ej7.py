dia = int(input('Inserta dia: '))
mes = int(input('Inserta mes: '))
año = int(input('Inserta año: '))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes ==12:
    if dia >= 1 and dia <= 31:
        print (dia,'/',mes,'/',año,' correcto.')
    else:
        print (dia,'/',mes,'/',año,' incorrecto.')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >=1 and dia <=30:
        print (dia,'/',mes,'/',año,' correcto.')
    else:
        print (dia,'/',mes,'/',año,' incorrecto.')
elif mes == 2:
    if dia >=1 and dia <=28:
        print (dia,'/',mes,'/',año,' correcto.')
    else:
        print (dia,'/',mes,'/',año,' incorrecto.')
else:
    print (dia,'/',mes,'/',año,' incorrecto.')
        
    
