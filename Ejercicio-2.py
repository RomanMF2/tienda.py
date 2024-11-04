import os

# Lista para almacenar los productos
productos = []

# Función para cargar los datos desde el archivo al iniciar el programa
def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(", ")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })

# Función para guardar los datos en el archivo al finalizar el programa
def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

# Función para añadir un producto
def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese valores válidos para el precio y la cantidad.")
    
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print(f"Producto '{nombre}' añadido con éxito.")

# Función para ver todos los productos
def ver_productos():
    if productos:
        print("\nLista de productos:")
        for idx, producto in enumerate(productos, start=1):
            print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("\nNo hay productos en el inventario.")

# Función para actualizar un producto existente
def actualizar_producto():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {producto}")
            while True:
                campo = input("¿Qué desea actualizar? (nombre/precio/cantidad): ").lower()
                if campo == "nombre":
                    producto["nombre"] = input("Ingrese el nuevo nombre: ")
                elif campo == "precio":
                    try:
                        producto["precio"] = float(input("Ingrese el nuevo precio: "))
                    except ValueError:
                        print("Ingrese un valor válido para el precio.")
                        continue
                elif campo == "cantidad":
                    try:
                        producto["cantidad"] = int(input("Ingrese la nueva cantidad: "))
                    except ValueError:
                        print("Ingrese un valor válido para la cantidad.")
                        continue
                else:
                    print("Campo no válido. Intente nuevamente.")
                    continue
                print("Producto actualizado con éxito.")
                return
    print("Producto no encontrado.")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
            return
    print("Producto no encontrado.")

# Menú principal
def menu():
    cargar_datos()  # Cargar datos al iniciar el programa
    while True:
        print("\nSistema de Gestión de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo del sistema.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
