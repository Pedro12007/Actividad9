peliculas = []

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
            pass

        case '2':
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