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
        title = input('Ingrese el título de la película: ')
        year = int_input_exception('el año de la película')
        genre = input('Ingrese el género de la película: ').capitalize()
        print()

        movie_details = [title, year, genre]
        movies_list.append(movie_details)
    return movies_list

def search_movies(movie_list):
    genre = input('Ingrese el género de la película: ')
    for movie in movie_list:
        if movie[2] == genre:
            print(f'Película: {movie[0]}')
    print()

def delete_movies(name):
    list_length_1 = len(peliculas)
    for i in range(len(peliculas)):
        if name == peliculas[i][0]:
            peliculas.pop(i)
            break
    list_length_2 = len(peliculas)
    if list_length_1 > list_length_2:
        print('Eliminación exitosa.\n')
    else:
        print('No existe la película.\n')

def statistics():
    print(f'Hay {len(peliculas)} películas registradas.\n')

    genres = {}
    for i in range(len(peliculas)):
        if not(peliculas[i][2] in genres):
            genres[peliculas[i][2]] = 1
        else:
            genres[peliculas[i][2]] += 1
    print('Géneros:')
    for genre, frequency in genres.items():
        print(f'{genre}: {frequency} películas')
    print()
    index = 0
    for i in range(len(peliculas)):
        oldest = peliculas[0][1]
        if oldest > peliculas[i][1]:
            oldest = peliculas[i][1]
            index = i
    print(f'La película más antigua es: {peliculas[index][0]}\n')




while True:
    print('Opciones:')
    print('1. Agregar películas.')
    print('2. Mostrar todas las películas registradas.')
    print('3. Buscar películas por género.')
    print('4. Eliminar una película por título.')
    print('5. Ver estadísticas del catálogo.')
    print('6. Salir del programa')

    option = input('Ingrese la opción que desea: ')
    print()

    match option:
        case '1':
            movies_amount = int_input_exception('cuantas películas desea ingresar')
            print()
            movies = add_movie(movies_amount)
            peliculas.extend(movies)

        case '2':
            if len(peliculas) > 0:
                print('Peliculas:')
                for i in range(len(peliculas)):
                     print(f'Título: {peliculas[i][0]}\nAño: {peliculas[i][1]}\nGénero: {peliculas[i][2]}\n')
            else:
                print('No hay películas registradas.\n')

        case '3':
            search_movies(peliculas)

        case '4':
            if len(peliculas) > 0:
                movie_name = input('Ingrese el nombre de la película: ')
                delete_movies(movie_name)
            else:
                print('No hay películas registradas.\n')

        case '5':
            if len(peliculas) > 0:
                statistics()
            else:
                print('No hay películas registradas.\n')

        case '6':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida. Intente nuevamente.\n')