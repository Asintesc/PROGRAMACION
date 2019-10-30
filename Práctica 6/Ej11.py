#Práctica 6 Ej11
#Albert Sintes Coll
import random
import time
random.seed (time.time ())
minimo = int(input( "Escribe un valor mínimo:"))
maximo = int(input( "Escribe un valor máximo:"))
print('A ver si adivinas el número entre %d y %d.' %(minimo,maximo))
secreto = random.randint (minimo, maximo)
intentos = 1
while True:
    numero = int(input('Escribe un número: '))
    if numero == secreto:
        print('Acierto! Lo has intentado %d veces.' %(intentos))
        break
    if numero > secreto:
        print('Oh vaya, parece que el número es menor.')
    if numero < secreto:
        print('Lo siento, el número es mayor.')
    intentos += 1
