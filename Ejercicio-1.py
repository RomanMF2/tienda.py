# Función para guardar la puntuación y comentario
def guardar_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point < 1 or point > 5:  # Expresión condicional que verifica si está fuera del rango
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'puntuación: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                print("Comentario guardado con éxito.")
                break
        else:
            print('Por favor, introduzca la puntuación en números')

# Función para leer los resultados guardados
def mostrar_resultados():
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print("Resultados hasta la fecha:")
                print(contenido)
            else:
                print("No hay resultados guardados.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. No hay resultados guardados.")

# Menú principal
def menu():
    while True:
        print('\nSeleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        
        num = input("Seleccione una opción: ")
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                guardar_puntuacion()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Finalizando')
                break  # Salir del bucle
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

# Ejecutar el programa
if __name__ == "__main__":
    menu()
