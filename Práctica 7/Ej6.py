#Práctica 7 Ej6
#Albert Sintes Coll

nombre = str(input('Escribe un nombre: '))
carácter = str(input('Escribe un carácter: '))
def comparacion(n,c):
    if c.lower() in n.lower():
        print ('%s está dentro de %s.'%(c,n))
    else:
        print ('%s no está dentro de %s.'%(c,n))
comparacion(nombre,carácter)
        
