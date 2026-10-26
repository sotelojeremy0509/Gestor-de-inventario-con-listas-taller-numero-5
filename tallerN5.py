"""
Gestor de inventario con listas paralelas.

Autor: Jeremy Antoine Sotelo Scarpeta 
Universidad de La Salle - Lógica de Programación (Python)

Estructura de datos:
    productos[i]   -> nombre del producto en la posición i
    cantidades[i]  -> cantidad disponible de ESE mismo producto

Decisión sobre duplicados: no se permite registrar dos veces el mismo
producto. La comparación ignora mayúsculas y espacios extra
("Arroz" y " arroz " son el mismo producto). Si el usuario intenta
registrar uno repetido, se le avisa y debe usar la opción 4 para
cambiar la cantidad. Así cada nombre tiene una sola cantidad y las
búsquedas, modificaciones y eliminaciones no son ambiguas.
"""

productos = []
cantidades = []


def normalizar(nombre):
    return nombre.strip().lower()


def buscar_indice(nombre):
    objetivo = normalizar(nombre)
    for i in range(len(productos)):
        if normalizar(productos[i]) == objetivo:
            return i
    return -1


def leer_entero(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.isdigit():
            return int(texto)
        print("Entrada no válida. Escribe un número entero mayor o igual a 0.")


# Opciones del menú

def registrar_producto():
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    if buscar_indice(nombre) != -1:
        print("Ese producto ya está registrado. Usa la opción 4 para "
              "modificar su cantidad.")
        return
    cantidad = leer_entero("Cantidad disponible: ")
    productos.append(nombre)
    cantidades.append(cantidad)
    print("Producto '" + nombre + "' registrado con " + str(cantidad)
          + " unidades.")


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario está vacío.")
        return
    print("\n--- INVENTARIO ---")
    for i in range(len(productos)):
        print(i + 1, "-", productos[i], "-", cantidades[i], "unidades")


def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")
    i = buscar_indice(nombre)
    if i == -1:
        print("El producto no existe en el inventario.")
    else:
        print("Encontrado:", productos[i], "-", cantidades[i], "unidades",
              "(posición", i + 1, "del inventario)")


def modificar_cantidad():
    nombre = input("Nombre del producto a modificar: ")
    i = buscar_indice(nombre)
    if i == -1:
        print("El producto no existe, no se puede modificar.")
        return
    print("Cantidad actual de", productos[i], ":", cantidades[i])
    nueva = leer_entero("Nueva cantidad: ")
    cantidades[i] = nueva
    print("Cantidad actualizada:", productos[i], "-", cantidades[i])


def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    i = buscar_indice(nombre)
    if i == -1:
        print("El producto no existe, no se eliminó nada.")
        return
    # Se elimina en AMBAS listas con el mismo índice para mantenerlas
    # sincronizadas.
    eliminado = productos.pop(i)
    cantidades.pop(i)
    print("Producto eliminado:", eliminado)


def mostrar_resumen():
    if len(productos) == 0:
        print("El inventario está vacío, no hay nada que resumir.")
        return
    print("Productos diferentes registrados:", len(productos))
    print("Total de unidades en inventario:", sum(cantidades))


def mostrar_mayor_cantidad():
    if len(productos) == 0:
        print("El inventario está vacío.")
        return
    mayor = max(cantidades)
    print("Producto(s) con mayor cantidad (" + str(mayor) + " unidades):")
    for i in range(len(productos)):
        if cantidades[i] == mayor:  # por si hay empate
            print("-", productos[i])



# Menú principal
def mostrar_menu():
    print("\n===== GESTOR DE INVENTARIO =====")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Modificar cantidad")
    print("5. Eliminar producto")
    print("6. Cuántos productos diferentes hay")
    print("7. Producto con mayor cantidad")
    print("8. Salir")


def main():
    opcion = ""
    while opcion != "8":
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            mostrar_mayor_cantidad()
        elif opcion == "8":
            print("Hasta luego.")
        else:
            print("Opción no válida. Elige un número del 1 al 8.")


main()