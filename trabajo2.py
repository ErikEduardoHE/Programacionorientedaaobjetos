# Hacer un areglo que ingrese, elimine, modifique y detecte elementos en una lista


lista = []

def insertarenlista(lista):
    lista.append(objingresado)
    print(f"{objingresado} agregado a la lista")

def removerdelista(lista):
    lista.remove()
    print(f"{lista} removido de la lista")

def eliminarultimoelemento(lista):
    lista.pop()
    print(f"Se elimino el ultimo elemento: {lista}")

def eliminarelementoporindice(lista):
    print(f"{lista} eliminado de la lista")
    del lista[0]

while True:
    print("Elige una opcion: ")
    print("1.- Agregar un objeto")
    print("2.- Remover elemento")
    print("3.- Eliminar ultimo elemento")
    print("4.- Eliminar elemento por indice")
    print("5.- Imprimir lista")
    print("6.- Salir")
    opcion = input(">>> ")
    if opcion == "1":
        objingresado = input("Que elemento deseas ingresar: ")
        insertarenlista(lista)
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        print(lista)
    elif opcion == "6":
        break
    else:
        print("Elige una opcion valida")