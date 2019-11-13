#Albert Sintes Coll -- examen 1º DAW
import os;
def menu():
    print('=======VIDEOCLUB========')
    print('==1. Añadir película====')
    print('==2. Reservar pelicula==')
    print('==3. Buscar película====')
    print('==4. Salir==============')
def añadir(p,c):
    os.system("clear||cln")
    id_ = 0
    copias = int(input('Dime la cantidad de copias que deseas añadir: '))
    c.append(copias)
    if (sum(c)) < 3000:
        titulo = input ('Título de la película: ')
        director = input ('Director: ')
        duracion = input ('Duración: ')
        genero = input ('Género: ')
        año = input ('Año: ')
        for i in range (copias):
            id_+=1
            p.append(['ID:',id_,'Título:',titulo,'Director:',director,'Duracion:',duracion,'Genero:',genero,'Año:',año])
        if id_ > 0:
            True
        else:
            False
    else:
        print('Ya no caben más copias en esta biblioteca.')
def reserva(p,r):
    lista = listar_pelis(p)
    id_ = int(input('Dame el id de la película que quieres reservar: '))
    if id_ == p[1:]:
        r.append([id_,titulo,director,duracion,genero,año])
        p.remove()
        print ('La película ha sido reservada.')
    else:
        print ('El ID de la película no existe en este videoclub.')
def listar_pelis(p):
    os.system("clear||cln")
    id = 1
    print ('====LISTADO DE PELIS====')
    for i in (p):
        print(*i)
    print ('========================')
def buscar(p):
    busqueda = int(input("""Qué tipo de búsqueda deseas realizar.
    1) Por título
    2) Por director
    3) Por género
    4) Por año
    5) Por duracion
    """))
    if (busqueda >= 1) and (busqueda <= 5):
        texto = input('Introduce el texto que quieres que aparezca en la búsqueda: ')
        if texto in (p):
            print([p])
        else:
            print('No existe ningún título que cumpla con los criterios de búsqueda seleccionados.')
peliculas = []
copias = []
reservas = []
opcion = 0
while opcion != '4':
    os.system("clear||cln")
    menu()
    opcion = input ('Selecciona una opción: ')
    if opcion == '1':
        añadir(peliculas,copias)
    elif opcion == '2':
        reserva(peliculas,reservas)
    elif opcion == '3':
        buscar(peliculas)
        
