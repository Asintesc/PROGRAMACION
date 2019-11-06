#Práctica 7 Ej11
#Albert Sintes Coll
frase = str(input('Escribe una frase: '))
def capicua(f):
    if f.replace(' ','') == f.replace(' ','')[::-1]:
        print('%s es capicúa o palíndrome.'%(f))
    else:
        print('%s no es capicúa o palíndrome.'%(f))
capicua(frase)
    
