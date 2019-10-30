#Práctica 6 Ej4
#Albert Sintes Coll
lista = []
numero1 = int(input('Escribe un número: '))
lista.append(numero1)
numero2  = int(input('Escribe un número mayor: '))
lista.append(numero2)
while numero2 <= numero1:
    print(numero2,' no es mayor que ',numero1)
    numero2  = int(input('Escribe un número mayor: '))
    lista.append(numero2)
print('Los números que has escrito son: ',numero1,' y ',numero2)
