from tabulate import tabulate
from backend.productos import listarProductos, consultarProducto, crearProducto, actualizarProducto, eliminarProducto

#Funcion para mostrar el menu
def mostrarMenu():
    print("\n" + "="*50)
    print("        SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("="*50)
    print("1. Listar todos los productos")
    print("2. Consultar producto por ID")
    print("3. Crear nuevo producto")
    print("4. Actualizar producto existente")
    print("5. Eliminar producto")
    print("6. Salir")
    print("="*50)

#Funcion para obtener una opcion del menu
def obtenerOpcion():
    try:
        opcion = int(input("\nSeleccione una opción (1-6): "))
        return opcion
    except ValueError:
        print("Error: Por favor ingrese un número válido.")
        return None
    
#Funcion para mostrar los productos
def mostrarProductos(productos):
    if not productos:
        print("\nNo hay productos para mostrar.")
        return
    
    headers = ["ID", "Nombre", "Precio", "Cantidad"]
    
    tabla = tabulate(productos, headers=headers, tablefmt="grid")
    print("\n" + tabla)

#Funcion para consultar los productos por id
def consultarProductoPorId():
    try:
        id_producto = int(input("\nIngrese el ID del producto a consultar: "))
        producto = consultarProducto(id_producto)
        
        if producto:
            datos_producto = [producto[1:]]
            headers = ["ID", "Nombre", "Precio", "Cantidad"]
            tabla = tabulate(datos_producto, headers=headers, tablefmt="grid")
            print(f"\nProducto encontrado:")
            print(tabla)
        else:
            print(f"\nNo se encontró ningún producto con el ID {id_producto}")
    except ValueError:
        print("Error: Por favor ingrese un ID válido (número entero).")

#Funcion para crear un nuevo producto
def crearNuevoProducto():
    print("\n--- CREAR NUEVO PRODUCTO ---")
    try:
        id_producto = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        if crearProducto(id_producto, nombre, precio, cantidad):
            print(f"\n¡Producto '{nombre}' creado exitosamente!")
        else:
            print(f"\nError: Ya existe un producto con el ID {id_producto}")
    except ValueError:
        print("Error: Por favor ingrese valores válidos.")

#Funcion para actualizar un producto existente
def actualizarProductoExistente():
    print("\n--- ACTUALIZAR PRODUCTO ---")
    try:
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        
        # Verificar si el producto existe
        producto_actual = consultarProducto(id_producto)
        if not producto_actual:
            print(f"\nError: No se encontró ningún producto con el ID {id_producto}")
            return
        
        print(f"\nProducto actual:")
        datos_producto = [producto_actual[1:]]
        headers = ["ID", "Nombre", "Precio", "Cantidad"]
        tabla = tabulate(datos_producto, headers=headers, tablefmt="grid")
        print(tabla)
        
        print(f"\nIngrese los nuevos valores (deje vacío para mantener el valor actual):")
        nombre = input(f"Nombre actual '{producto_actual[2]}': ").strip()
        if not nombre:
            nombre = producto_actual[2]
            
        precio_str = input(f"Precio actual '{producto_actual[3]}': ").strip()
        if not precio_str:
            precio = producto_actual[3]
        else:
            precio = float(precio_str)
            
        cantidad_str = input(f"Cantidad actual '{producto_actual[4]}': ").strip()
        if not cantidad_str:
            cantidad = producto_actual[4]
        else:
            cantidad = int(cantidad_str)
        
        if actualizarProducto(id_producto, nombre, precio, cantidad):
            print(f"\n¡Producto con ID {id_producto} actualizado exitosamente!")
        else:
            print(f"\nError: No se pudo actualizar el producto")
    except ValueError:
        print("Error: Por favor ingrese valores válidos.")

#Funcion para eliminar un producto
def eliminarProductoExistente():
    print("\n--- ELIMINAR PRODUCTO ---")
    try:
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        
        # Verificar si el producto existe
        producto_actual = consultarProducto(id_producto)
        if not producto_actual:
            print(f"\nError: No se encontró ningún producto con el ID {id_producto}")
            return
        
        print(f"\nProducto a eliminar:")
        datos_producto = [producto_actual[1:]]
        headers = ["ID", "Nombre", "Precio", "Cantidad"]
        tabla = tabulate(datos_producto, headers=headers, tablefmt="grid")
        print(tabla)
        
        confirmacion = input(f"\n¿Está seguro de que desea eliminar el producto '{producto_actual[2]}'? (s/n): ").lower()
        
        if confirmacion in ['s', 'si', 'sí', 'y', 'yes']:
            if eliminarProducto(id_producto):
                print(f"\n¡Producto '{producto_actual[2]}' eliminado exitosamente!")
            else:
                print(f"\nError: No se pudo eliminar el producto")
        else:
            print("\nOperación cancelada.")
    except ValueError:
        print("Error: Por favor ingrese un ID válido.")

#funcion para ejecutar la aplicacion, llamando las funciones creadas anteriormente
def ejecutarAplicacion():
    while True:
        mostrarMenu()
        opcion = obtenerOpcion()
        
        if opcion == 1:
            print("\nCargando todos los productos...")
            productos = listarProductos()
            mostrarProductos(productos)
            
        elif opcion == 2:
            consultarProductoPorId()
            
        elif opcion == 3:
            crearNuevoProducto()
            
        elif opcion == 4:
            actualizarProductoExistente()
            
        elif opcion == 5:
            eliminarProductoExistente()
            
        elif opcion == 6:
            print("\n¡Gracias por usar el Sistema de Gestión de Productos!")
            break
            
        else:
            print("\nOpción no válida. Por favor seleccione una opción del 1 al 6.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    ejecutarAplicacion()