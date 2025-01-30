#Calcular el area de diferentes formas con diferente numero de lados
#Area y perimetro

import math

nL = input("Ingresa el numero de lados de la figura(3,4,5): ")
L = input("Ingresa la medida de los lados de cada figura: ")
ap = 75

class figura:
    def areacuadrado(L):
        return L * L
    
    def arearectangulo(L):
        h = pow(L, 1/3) / 2
        return L * h / 2
    
    def areapentagono(L, ap):
        return nL / 2

    
    def perimetro(L,nL):
        return L * nL
    