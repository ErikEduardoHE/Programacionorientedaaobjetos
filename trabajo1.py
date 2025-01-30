#Calcular el area de diferentes formas con diferente numero de lados
#Area y perimetro

import math


while True:
    nL = input("Ingresa el numero de lados de la figura(3,4,5): ")
    L = input("Ingresa la medida de los lados de cada figura: ")
    if nL == "3":
       perimetro(L,nL)
       areacuadrado
    elif nL == "4":
        pass
    elif nL == "5":
        pass
    else:
        print("Error")
        

class figura:
    ap = 75
    def areacuadrado(L):
        return L * L
            
    def arearectangulo(L):
        h =  3**2 * L / 2
        return L * h / 2
        
    def areapentagono(L):
        return nL / 2 (math.tan( ap ))

    def perimetro(L,nL):
        return L * nL
        
