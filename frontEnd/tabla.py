from tabulate import tabulate

#Funcion para crear la tabla usando tabulate
def crearTabla(datos, encabezados, formato="grid"):
    return tabulate(datos, headers=encabezados, tablefmt=formato)

#funcion para mostrar la tabla creada
def mostrarTabla(datos, encabezados, formato="grid"):
    tabla = crearTabla(datos, encabezados, formato)
    print("\n" + tabla)