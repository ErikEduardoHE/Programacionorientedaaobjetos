# Hacer un areglo que ingrese, elimine, modifique y detecte elementos en una lista


lista = []

def insertarenlista(lista):
    lista.append(objingresado)
    print(f"{objingresado} agregado a la lista")

def removerdelista(lista):
    lista.remove(objremovido)
    print(f"{objremovido} removido de la lista")

def eliminarultimoelemento(lista):
    lista.pop()
    print(f"Se elimino el ultimo elemento")

def eliminarelementoporindice(lista):
    print(f"{lista[indice]} eliminado de la lista")
    del lista[indice]

while True:
    print("-----------------------------------")
    print("Elige una opcion: ")
    print("1.- Agregar un objeto")
    print("2.- Remover elemento")
    print("3.- Eliminar ultimo elemento")
    print("4.- Eliminar elemento por indice")
    print("5.- Imprimir lista")
    print("6.- Salir")
    print("-----------------------------------")
    opcion = input(">>> ")
    if opcion == "1":
        print("-----------------------------------")
        objingresado = input("Que elemento deseas ingresar: ")
        insertarenlista(lista)
        print("-----------------------------------")
    elif opcion == "2":
        print("-----------------------------------")
        objremovido = input("Que elemento quieres remover: ")
        removerdelista(lista)
        print("-----------------------------------")
    elif opcion == "3":
        print("-----------------------------------")
        eliminarultimoelemento(lista)
        print("-----------------------------------")
    elif opcion == "4":
        print("-----------------------------------")
        print(lista)
        indice = int(input("Escribe el indice del objeto que quieres eliminar: "))
        indice = indice - 1
        eliminarelementoporindice(lista)
        print("-----------------------------------")
    elif opcion == "5":
        print("-----------------------------------")
        print(lista)
        print("-----------------------------------")
    elif opcion == "6":
        break
    else:
        print("Elige una opcion valida")