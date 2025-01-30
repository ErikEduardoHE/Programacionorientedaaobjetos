#Calcular el area de diferentes formas con diferente numero de lados
#Area y perimetro

import math


while True:
    nL = int(input("Ingresa el numero de lados de la figura(3,4,5): "))
    
    if nL == 3:
       L = int(input("Ingresa la medida de los lados de cada figura: "))
       perimetro(L,nL)
       arearectangulo(L)

    elif nL == 4:
        L = int(input("Ingresa la medida de los lados de cada figura: "))
        perimetro(L,nL)
        areacuadrado(L)

    elif nL == 5:
        L = int(input("Ingresa la medida de los lados de cada figura: "))
        perimetro(L,nL)
        areapentagono(L)
        
    else:
        print("Error")
        
    ap = 75
    
    def areacuadrado(L):
        return L * L
        print(areacuadrado(L))
            
    def arearectangulo(L):
        h =  3**2 * L / 2
        return L * h / 2
        print(arearectangulo(L))
        
    def areapentagono(L):
        return nL / 2 (math.tan( ap ))
        print(areapentagono(L))

    def perimetro(L,nL):
        return L * nL
        print(perimetro(L,nL))
