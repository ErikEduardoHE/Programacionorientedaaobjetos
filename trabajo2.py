# Hacer un areglo que ingrese, elimine, modifique y detecte elementos en una lista
from numpy import array
import numpy as np

lista = []

def insertarenlista(lista):
    lista.append()
    print(f"{lista} agregado a la lista")

def removerdelista(lista):
    lista.remove()
    print(f"{lista} removido de la lista")

def eliminarultimoelemento(lista):
    lista.pop()
    print(f"Se elimino el ultimo elemento: {lista}")

def eliminarelementoporindice(lista):
    print(f"{} eliminado de la lista")
    del lista[0]

while True:
    opcion = input("Elige una opcion: ")
    print("1.- Agregar un objeto")
    print("2.- Remover elemento")
    print("3.- Eliminar ultimo elemento")
    print("4.- Eliminar elemento por indice")
    print("5.- Salir")

    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        break
    else:
        print("Elige una opcion valida")