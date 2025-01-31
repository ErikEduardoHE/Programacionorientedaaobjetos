#Calcular el area y perimetro de diferentes formas con diferente numero de lados

import math

def areacuadrado(L):
        return L * L
                    
def areatriangulo(L):
    altura = (math.sqrt(3) / 2) * L
    return (L * altura) / 2
        
def areapentagono(L):
    (nL / 2) * math.tan(math.radians(35)) * L**2

def perimetro(L,nL):
    return L * nL


while True:
    nL = int(input("Ingresa el numero de lados de la figura(3,4,5): "))
    
    if nL == 1:
        print("No puedo calcular esa figura aun")
    elif nL == 2:
        print("Figura no existente")
    elif  nL == 3:
       L = int(input("Ingresa la medida de los lados de cada figura: "))
       perimetro(L,nL)
       print("-------------------------")
       print(f"Perimetro: {perimetro(L,nL)}")
       print("-------------------------")
       areatriangulo(L)
       print("-------------------------")
       print(f"Area: {areatriangulo(L)}")
       print("-------------------------")

    elif nL == 4:
        L = int(input("Ingresa la medida de los lados de cada figura: "))
        perimetro(L,nL)
        print("-------------------------")
        print(f"Perimetro: {perimetro(L,nL)}")
        print("-------------------------")
        areacuadrado(L)
        print("-------------------------")
        print(f"Area: {areacuadrado(L)}")
        print("-------------------------")

    elif nL == 5:
        L = int(input("Ingresa la medida de los lados de cada figura: "))
        
        perimetro(L,nL)
        print("-------------------------")
        print(f"Perimetro: {perimetro(L,nL)}")
        print("-------------------------")
        areapentagono(L)
        print("-------------------------")
        print(f"Area: {areapentagono(L)}")
        print("-------------------------")
        
    else:
        print("-------------------------")
        print("Aun no puedo calcular esa figura")
        print("-------------------------")