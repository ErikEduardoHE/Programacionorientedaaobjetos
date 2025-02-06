
lista = []

def insertarenlista(lista, objingresado):
    lista.append(objingresado)
    print(f"{objingresado} agregado a la lista")

def removerdelista(lista, objremovido):
    if objremovido in lista:
        lista.remove(objremovido)
        print(f"{objremovido} removido de la lista")
    else:
        print(f"{objremovido} no se encuentra en la lista")

def modificarunelemento(lista, eliminado, nuevoindice):
    if eliminado < len(lista):
        valor = lista.pop(eliminado)  
        lista.insert(nuevoindice, valor) 
        print(f"Se modificó el elemento {valor} en la lista")
    else:
        print("Índice no válido para modificar")

def eliminarelementoporindice(lista, indice):
    if indice < len(lista):
        print(f"{lista[indice]} eliminado de la lista")
        del lista[indice]
    else:
        print("Índice no válido para eliminar")

while True:
    print("-----------------------------------")
    print("Elige una opción: ")
    print("1.- Agregar un objeto")
    print("2.- Remover elemento")
    print("3.- Modificar elemento")
    print("4.- Eliminar elemento por índice")
    print("5.- Imprimir lista")
    print("6.- Salir")
    print("-----------------------------------")
    opcion = input(">>>>>> ")

    if opcion == "1":
        print("-----------------------------------")
        objingresado = input("¿Qué elemento deseas ingresar? ")
        insertarenlista(lista, objingresado)
        print("-----------------------------------")

    elif opcion == "2":
        print("-----------------------------------")
        objremovido = input("¿Qué elemento quieres remover? ")
        removerdelista(lista, objremovido)
        print("-----------------------------------")

    elif opcion == "3":
        print("-----------------------------------")
        print(f"Lista actual:{lista}")
        try:
            eliminado = int(input("¿Qué elemento quieres mover? (escribe su índice): "))
            nuevoindice = int(input("¿En qué índice quieres colocarlo?: "))
            eliminar_elemento = eliminado - 1
            nuevo_indice = nuevoindice - 1
            modificarunelemento(lista, eliminar_elemento, nuevo_indice)
        except ValueError:
            print("Por favor ingresa un número válido.")
        print("-----------------------------------")

    elif opcion == "4":
        print("-----------------------------------")
        print(f"Lista actual:{lista}")
        try:
            indice = int(input("Escribe el índice del objeto que quieres eliminar: "))
            indice = indice - 1
            eliminarelementoporindice(lista, indice)
        except ValueError:
            print("Por favor ingresa un número válido.")
        print("-----------------------------------")

    elif opcion == "5":
        print("-----------------------------------")
        print(f"Lista actual:{lista}")
        print("-----------------------------------")

    elif opcion == "6":
        break

    else:
        print("Elige una opción válida")
