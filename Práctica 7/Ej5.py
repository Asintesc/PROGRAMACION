#Práctica 7 Ej5
#Alebrt Sintes Coll
frase = str(input('Dime algo: '))
vocal = str(input('Dime una vocal: '))
def cambio(frase1,vocal1):
        frase1 = frase1.replace('a', vocal1)
        frase1 = frase1.replace('e', vocal1)
        frase1 = frase1.replace('i', vocal1)
        frase1 = frase1.replace('o', vocal1)
        frase1 = frase1.replace('u', vocal1)
        return frase1
print('La frase es ahora: ',cambio(frase,vocal))    
    
