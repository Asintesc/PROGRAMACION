#Práctica 7 Ej13
#Albert Sintes Coll
def primo_while(v):
    if v == 2:
        return True
    if v % 2 == 0:
        return False
    i = 3
    while i ** 2 <= v:
        if v % i == 0:
            return False
        i = i + 2
    return True
def primo_for(v):
    for i in range(1, v+1):
        if v % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

num = int(input('Dime un número: '))
select = str(input("""Cómo quieres calcular si es primo?
1.While
2.For
 """))
if select == '1':
    if primo_while(num):
        print ('%d es primo.' %(num))
    else:
        print ('%d no es primo.' %(num))
elif select == '2':
    if primo_for(num):
        print ('%d es primo.' %(num))
    else:
        print ('%d no es primo.' %(num))
else:
    print('Opción no disponible.')
            
                   
