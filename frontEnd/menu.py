from tabulate import tabulate
from backend.productos import listarProductos, consultarProducto

#Funcion para mostrar el menu
def mostrarMenu():
    print("\n" + "="*50)
    print("        SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("="*50)
    print("1. Listar todos los productos")
    print("2. Consultar producto por ID")
    print("3. Salir")
    print("="*50)

#Funcion para obtener una opcion del menu
def obtenerOpcion():
    try:
        opcion = int(input("\nSeleccione una opción (1-3): "))
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
            print("\n¡Gracias por usar el Sistema de Gestión de Productos!")
            break
            
        else:
            print("\nOpción no válida. Por favor seleccione una opción del 1 al 3.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    ejecutarAplicacion()