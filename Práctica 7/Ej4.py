#Práctica 7 Ej4
#Albert Sintes Coll
frase = str(input('Escribe una frase: '))
def asterisco(frase):
    for i in (frase):
        print(i.replace(' ','*'), end = '')
asterisco(frase)
