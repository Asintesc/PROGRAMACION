#Práctica 7 Ej9
#Albert Sintes Coll
palabra1 = str(input('Escribe una palabra: '))
palabra2 = str(input('Escribe otra palabra: '))
def rima(p1,p2):
    if p1[-3:] == p2[-3:]:
        print ('Las palabras %s y %s riman.' %(p1,p2))
    elif p1[-2:] == p2[-2:]:
        print ('Las palabras %s y %s riman un poco.' %(p1,p2))
    else:
        print ('Las palabras %s y %s no riman.' %(p1,p2))
rima(palabra1,palabra2)
               
