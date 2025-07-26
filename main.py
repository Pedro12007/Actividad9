peliculas = []

def int_input_exception(text):
    while True:
        try:
            value = int(input(f'Ingrese {text}: '))
            return value
        except ValueError:
            print('Debe ser un número.\n')

def add_movie(amount):
    movies_list = []
    for i in range(amount):
        title = input('Ingrese el título de la película')
        year = int_input_exception('el año de la película')
        genre = input('Ingrese el género de la película: ')

        movie_details = [title, year, genre]
        movies_list.append(movie_details)
    return movies_list

while True:
    print('Opciones:')
    print('1. Agregar películas.')
    print('2. Mostrar todas las películas registradas.')
    print('3. Buscar películas por género.')
    print('4. Eliminar una película por título.')
    print('5. Ver estadísticas del catálogo.')
    print('6. Salir del programa')

    option = input('Ingrese la opción que desea: ')

    match option:
        case '1':
            movies_amount = int_input_exception('cuantas películas desea ingresar')
            movies = add_movie(movies_amount)
            peliculas.extend(movies)

        case '2':
            for i in range(len(peliculas)):
                 pass

        case '3':
            pass

        case '4':
            pass

        case '5':
            pass

        case '6':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida. Intente nuevamente.\n')