from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre          # Atributo privado
        self._precio = precio          # Atributo privado

    @abstractmethod
    def mostrar_detalles(self):
        pass

    def obtener_precio(self):
        return self._precio
class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla           # Atributo específico de Camisa

    def mostrar_detalles(self):
        print(f"Camisa: {self._nombre}, Talla: {self._talla}, Precio: ${self._precio}")

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre, precio)
        self._talla = talla           # Atributo específico de Pantalon
        self._color = color           # Atributo específico de Pantalon

    def mostrar_detalles(self):
        print(f"Pantalon: {self._nombre}, Talla: {self._talla}, Color: {self._color}, Precio: ${self._precio}")

class Zapato(Producto):
    def __init__(self, nombre, precio, talla, tipo):
        super().__init__(nombre, precio)
        self._talla = talla           # Atributo específico de Zapato
        self._tipo = tipo             # Atributo específico de Zapato

    def mostrar_detalles(self):
        print(f"Zapato: {self._nombre}, Talla: {self._talla}, Tipo: {self._tipo}, Precio: ${self._precio}")
class Tienda:
    def __init__(self):
        self._inventario = []         # Inventario de productos en la tienda

    def agregar_producto(self, producto):
        self._inventario.append(producto)  # Método para agregar producto al inventario

    def mostrar_inventario(self):
        print("Inventario de Tienda:")
        for producto in self._inventario:
            producto.mostrar_detalles()

    def procesar_compra(self, producto):
        if producto in self._inventario:
            print(f"Compra procesada: {producto._nombre} por ${producto.obtener_precio()}")
            self._inventario.remove(producto)
        else:
            print("El producto no está disponible.")
# Crear productos
camisa = Camisa("Camisa de algodón", 20, "M")
pantalon = Pantalon("Jeans", 35, "32", "Azul")
zapato = Zapato("Zapatos deportivos", 50, 42, "Deportivos")

# Crear tienda y agregar productos al inventario
tienda = Tienda()
tienda.agregar_producto(camisa)
tienda.agregar_producto(pantalon)
tienda.agregar_producto(zapato)

# Mostrar inventario y procesar una compra
tienda.mostrar_inventario()
tienda.procesar_compra(camisa)

