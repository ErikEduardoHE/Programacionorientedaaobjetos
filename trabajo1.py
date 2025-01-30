#Calcular el area de diferentes formas con diferente numero de lados
#Area y perimetro

import math

ap = 75

def areacuadrado(L):
        return L * L
                    
def areatriangulo(L):
    h =  3**2 * L / 2
    return L * h / 2
        
def areapentagono(L):
    return nL / 2 (math.tan( ap ))

def perimetro(L,nL):
    return L * nL


while True:
    nL = int(input("Ingresa el numero de lados de la figura(3,4,5): "))
    
    if nL == 3:
       L = int(input("Ingresa la medida de los lados de cada figura: "))
       perimetro(L,nL)
       print(f"Perimetro: {perimetro(L,nL)}")
       areatriangulo(L)
       print(f"Area: {areatriangulo(L)}")

    elif nL == 4:
        L = int(input("Ingresa la medida de los lados de cada figura: "))
        perimetro(L,nL)
        print(f"Perimetro: {perimetro(L,nL)}")
        areacuadrado(L)
        print(f"Area: {areacuadrado(L)}")

    elif nL == 5:
        L = int(input("Ingresa la medida de los lados de cada figura: "))
        perimetro(L,nL)
        print(f"Perimetro: {perimetro(L,nL)}")
        areapentagono(L)
        print(f"Area: {areapentagono(L)}")
        
    else:
        print("Error")