#Práctica 7 Ej10
#Albert Sintes Coll
valor = str(input('Escribe algo: '))
def capicua(v):
    if v == v[::-1]:
        print('%s es capicúa o palíndrome.'%(v))
    else:
        print ('%s no es capicúa o palíndrome.'%(v))
capicua(valor)
