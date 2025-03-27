""" Colecciones

Listas 
Tuplas
Conjuntos
Diccionarios

import numpy as np
from numpy import array
np.array()
arreglo = []
arreglo = list()

String > Floats > int > boolean (gerarquia ed mayor peso en memotia)

tupla = (,) (una tupla es inmutable)
tupla = tuple()
"""
import numpy as np
from numpy import array

lista_mixta = ["Hola mundo", 3.1416 , 1, True, False]

lista_numpy = np.array([1, 2, 3, 4, 5])

tupla_mixta = tuple(lista_mixta)

tupla_numpy = tuple(lista_numpy)

conjunto_mixto = set(lista_mixta)

conjunto_numpy = set(lista_numpy)

diccionario = {
    "1": 1,
    "2": True,
    "3": 3.1416,
    "4": "4",
    "5": False
}

print(lista_mixta)
print(lista_numpy)
print(tupla_mixta)
print(tupla_numpy)
print(conjunto_mixto)
print(conjunto_numpy)
print(diccionario)

lista2 = [1, 1.1, True, "String"]
lista2.append(1, "Hola")
lista2.extend([2, "Hola2"])
lista2.index(1)
lista2.count(1)
x = 1 in lista2