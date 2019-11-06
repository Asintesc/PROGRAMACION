#Práctica 7 Ej12
#Albert Sintes Coll
frase = str(input('Escribe una frase: '))
def cont(f):
    f = f.replace(',',' ')
    palabras = f.split(' ')
    contador = len(palabras)
    return contador
print ('La frase tiene ',cont(frase),' palabras.')
