#Práctica 6 Ej12
#Albert Sintes Coll
import random
import time
random.seed (time.time ())
minimo = int (input ( "Dime el valor mínimo:"))
maximo = int (input ( "Dime el valor máximo:"))
print('Piensa un número entre %d y %d a ver si lo puedo adivinar: ' %(minimo,maximo))
while True:
    numero = random.randint (minimo, maximo)
    intento = str(input('Es %d?: '%(numero)))
    if intento.lower() == 'mayor':
        minimo = numero
    elif intento.lower() == 'menor':
        maximo = numero
    elif intento.lower() == 'igual':
        print('Gracias por jugar.')
        break
                  
                
                  
