#Sistema de inventario para una tienda de barrio
def agregar_producto(inventario):
    try: 
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = input("Ingrese el stock del producto: ")
        precio = input("Ingrese el precio del producto: ")

        producto = {"nombre": nombre, "cantidad": int(cantidad), "precio": float(precio) }
        inventario.append(producto)
        print("Se agregó el producto con exito")
    except:
        print("Error al agregar el producto")



def listar_productos(inventario):
    #Valido si hay productos en el inventario
    if not inventario:
        print("No hay productos en el inventario\n")
    else:
        print("\nLista de productos")
        
        for indice, producto in enumerate(inventario):
            print(indice,". -",producto["nombre"], "cantidad:", producto["cantidad"], "precio:",producto["precio"])

def actualizar_producto(inventario):
    listar_productos(inventario)
    if not inventario:
        return
    else:
        try:
            indice = int(input("Ingrese el indice del producto a actualizar: "))
            if(indice < 0 or indice > len(inventario)):
                print("El indice no existe en la lista.")
            else: 

                nombre = input("Ingrese el nuevo nombre del producto: ")
                cantidad = input("Ingrese el nuevo stock del producto: ")
                precio = input("Ingrese el nuevo precio del producto: ")
                print("Actualizando el producto",inventario[indice]["nombre"])

                inventario[indice]["nombre"] = nombre
                inventario[indice]["cantidad"] = int(cantidad)
                inventario[indice]["precio"] = float(precio)

                print("\nEl producto fue actualizado con exito!\n")

        except:
            print("Oops!, algo salió mal")
            
def eliminar_producto(inventario):
    listar_productos(inventario)

    if not inventario:
        return
    else:
        try:
            indice = int(input("Ingrese el indice del producto a eliminar: "))
            if(indice < 0 or indice > len(inventario)):
                print("El indice no corresponde a ningún producto\n")
            else:
                print("Eliminando producto ...")
                inventario.pop(indice)
                print("El producto fue eliminado con éxito.\n")
        except:
            print("Oops!, algo salió mal")



def mostrarMenu():
    input("Presione ENTER para continuar...")
    print("\n----------MENÚ DE OPCIONES----------\n")
    print("1. Listar productos")
    print("2. Agregar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def main():
    inventario = []
    while True:
        
        mostrarMenu()
        opcion = input("Ingrese una opción: ")

        if(opcion == "1"):
            listar_productos(inventario)

        elif(opcion == "2"):
            agregar_producto(inventario)
        
        elif(opcion == "3"):
            actualizar_producto(inventario)
        elif(opcion == "4"):
            eliminar_producto(inventario)
        elif(opcion == "5"):
            break
        

main()