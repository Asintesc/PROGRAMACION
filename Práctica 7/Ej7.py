#Práctica 7 Ej7
#Albert Sintes Coll
frase = str(input('Escribe una frase: '))
def num_vocales(f):
    f = f.lower()
    print ('Hay ',f.count('a'),'vocales de la letra a.')
    print ('Hay ',f.count('e'),'vocales de la letra e.')
    print ('Hay ',f.count('i'),'vocales de la letra i.')
    print ('Hay ',f.count('o'),'vocales de la letra o.')
    print ('Hay ',f.count('u'),'vocales de la letra u.')
num_vocales(frase)
