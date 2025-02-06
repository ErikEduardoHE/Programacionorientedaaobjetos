class ListaManager:
    def __init__(self):
        self.lista = [] 

    def insertar_en_lista(self, objingresado):
        self.lista.append(objingresado)
        print(f"{objingresado} agregado a la lista")

    def remover_de_lista(self, objremovido):
        if objremovido in self.lista:
            self.lista.remove(objremovido)
            print(f"{objremovido} removido de la lista")
        else:
            print(f"{objremovido} no se encuentra en la lista")

    def modificar_un_elemento(self, eliminado, nuevoindice):
        if eliminado < len(self.lista):
            valor = self.lista.pop(eliminado)  
            self.lista.insert(nuevoindice, valor) 
            print(f"Se modificó el elemento {valor} en la lista")
        else:
            print("Índice no válido para modificar")

    def eliminar_elemento_por_indice(self, indice):
        if indice < len(self.lista):
            print(f"{self.lista[indice]} eliminado de la lista")
            del self.lista[indice]
        else:
            print("Índice no válido para eliminar")

    def imprimir_lista(self):
        print(f"Lista actual: {self.lista}")



lista_manager = ListaManager()

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
        lista_manager.insertar_en_lista(objingresado)
        print("-----------------------------------")

    elif opcion == "2":
        print("-----------------------------------")
        objremovido = input("¿Qué elemento quieres remover? ")
        lista_manager.remover_de_lista(objremovido)
        print("-----------------------------------")

    elif opcion == "3":
        print("-----------------------------------")
        lista_manager.imprimir_lista()
        try:
            eliminado = int(input("¿Qué elemento quieres mover? (escribe su índice): "))
            nuevoindice = int(input("¿En qué índice quieres colocarlo?: "))
            eliminar_elemento = eliminado - 1
            nuevo_indice = nuevoindice - 1
            lista_manager.modificar_un_elemento(eliminar_elemento, nuevo_indice)
        except ValueError:
            print("Por favor ingresa un número válido.")
        print("-----------------------------------")

    elif opcion == "4":
        print("-----------------------------------")
        lista_manager.imprimir_lista()
        try:
            indice = int(input("Escribe el índice del objeto que quieres eliminar: "))
            indice = indice - 1
            lista_manager.eliminar_elemento_por_indice(indice)
        except ValueError:
            print("Por favor ingresa un número válido.")
        print("-----------------------------------")

    elif opcion == "5":
        print("-----------------------------------")
        lista_manager.imprimir_lista()
        print("-----------------------------------")

    elif opcion == "6":
        break

    else:
        print("Elige una opción válida")
