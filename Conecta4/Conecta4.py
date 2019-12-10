

import sys
import random

######### DECLARACIÓN DE VARIABLES #########
jugador1 = ""
jugador2 = ""

cpu = 0
diffcpu = 1

puntuacionJ1 = 0
puntuacionJ2 = 0

turno = 1

ficha1 = "X"
ficha2 = "O"
#############################################

tablero = [
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
]

def mostrarTablero():
    for i in range(len(tablero)-1):
        f = ""
        for columna in tablero:
            f += " " + columna[i]
        print(f.replace("0", "*").replace("1", ficha1).replace("2", ficha2))
        
def meterFicha(jugador, columna):
    jugador = str(jugador)
    c = tablero[columna]
    if c[5] == '0':
        tablero[columna][5] = jugador
    elif c[4] == '0':
        tablero[columna][4] = jugador
    elif c[3] == '0':
        tablero[columna][3] = jugador
    elif c[2] == '0':
        tablero[columna][2] = jugador
    elif c[1] == '0':
        tablero[columna][1] = jugador
    elif c[0] == '0':
        tablero[columna][0] = jugador
    else:
        return False
    return True 


def pedirMovimiento(jugador):
    c = 10
    while c < 0 or c>6:
        if jugador == 1:
            c = int(input(jugador1+' elige la columna: '))
        elif jugador == 2:
            c = int(input(jugador2+ ' elige la columna: '))
    return c
         
def resetearTablero():
    for i, y in enumerate(tablero):
        for o, x in enumerate(y):
            tablero[i][o] = "0"

def pedirRevancha(w):
    if w == 1:
        i = input("{0} quieres la revancha (Si/No) => ".format(jugador2))
    else:
        i = input("{0} quieres la revancha (Si/No) => ".format(jugador1))

    if i.lower() == "si":
        return True
    else:
        return False


def endGame(winner):
    global puntuacionJ1
    global puntuacionJ2

    if winner == 1:
        puntuacionJ1 += 1
        print("Ha ganado el jugador {0}".format(jugador1))
    else:
        puntuacionJ2 += 1
        print("Ha ganado el jugador {0}".format(jugador2))
    if pedirRevancha(winner):
        resetearTablero()
        mostrarTablero()
        iniciarJuego()
    else:
        print("El jugador {0} ha quedado con {1} puntos y el jugador {2} ha quedado con {3} puntos.".format(jugador1, puntuacionJ1, jugador2, puntuacionJ2))
        sys.exit()
    #pedirRevancha(winner)

def checkTablero():
    # Chequeo de columnas
    for columna in tablero:
        f = "".join(columna)
        if "1111" in f:
            endGame(1)
        elif "2222" in f:
            endGame(2)
    
    # Chequeo de filas
    for i in range(len(tablero)-1):
        f = ""
        for columna in tablero:
            f += columna[i]

        if "1111" in f:
            endGame(1)
        elif "2222" in f:
            endGame(2)
    
    # chequeo de diagonales
    diagonals = []

    diagonals.append(tablero[3][0] + tablero[2][1] + tablero[1][2] + tablero[0][3])
    diagonals.append(tablero[4][0] + tablero[3][1] + tablero[2][2] + tablero[1][3] + tablero[0][4])
    diagonals.append(tablero[5][0] + tablero[4][1] + tablero[3][2] + tablero[2][3] + tablero[1][4] + tablero[0][5])
    diagonals.append(tablero[6][0] + tablero[5][1] + tablero[4][2] + tablero[3][3] + tablero[2][4] + tablero[1][5])
    diagonals.append(tablero[6][1] + tablero[5][2] + tablero[4][3] + tablero[3][4] + tablero[2][5])
    diagonals.append(tablero[6][2] + tablero[5][3] + tablero[4][4] + tablero[3][5])

    diagonals.append(tablero[6][3] + tablero[5][2] + tablero[4][1] + tablero[3][0])
    diagonals.append(tablero[6][4] + tablero[5][3] + tablero[4][2] + tablero[3][1] + tablero[2][0])
    diagonals.append(tablero[6][5] + tablero[5][4] + tablero[4][3] + tablero[3][2] + tablero[2][1] + tablero[1][0])
    diagonals.append(tablero[5][5] + tablero[4][4] + tablero[3][3] + tablero[2][2] + tablero[1][1] + tablero[0][0])
    diagonals.append(tablero[4][5] + tablero[3][4] + tablero[2][3] + tablero[1][2] + tablero[0][1])
    diagonals.append(tablero[3][5] + tablero[2][4] + tablero[1][3] + tablero[0][2])

    for i in diagonals:
        if "1111" in i:
            endGame(1)
        elif "2222" in i:
            endGame(2)

def Mostrar_Menu():
    print("=========================")
    print("=====   CONECTA 4   =====")
    print("=========================")
    print(" ELIGE EL MODO DE JUEGO  ")
    print("=========================")
    print("1)JUGADOR CONTRA JUGADOR ")
    print("2)JUDADOR CONTRA CPU     ")
    print("=========================")
    print("3)SALIR                  ")
    print("=========================")

def iniciarJuego():
    global turno
    global cpu

    if cpu == 0:
        c = pedirMovimiento(turno)
        f = meterFicha(turno, c)
        while f == False:
            print("¡Esa columna está completa!")
            c = pedirMovimiento(turno)
            f = meterFicha(turno, c)
        if turno == 1:
            turno = 2
        else:
            turno = 1
        checkTablero()
        mostrarTablero()
        iniciarJuego()
    else:
        print("")
        if turno == 1:
            c = pedirMovimiento(turno)
        else:
            c = random.randint(0, 6)
        f = meterFicha(turno, c)
        while f == False:
            print("¡Esa columna está completa!")
            c = pedirMovimiento(turno)
            f = meterFicha(turno, c)
        if turno == 1:
            turno = 2
        else:
            turno = 1
        checkTablero()
        mostrarTablero()
        iniciarJuego()
o=0
while o !="3":
    Mostrar_Menu()
    o=input("Elige una opción =>")
    if o=="1":
        jugador1 = input("Dime el nombre del jugador 1 => ")
        jugador2 = input("Dime el nombre del jugador 2 => ")
        mostrarTablero()
        iniciarJuego()

    if o=="2":
        jugador1 = input("Dime el nombre del jugador 1 => ")
        cpu = 1
        mostrarTablero()
        iniciarJuego()
                
   
