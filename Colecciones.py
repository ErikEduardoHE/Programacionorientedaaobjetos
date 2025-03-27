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
    "Nombre": ,
    "Edad": 10
}