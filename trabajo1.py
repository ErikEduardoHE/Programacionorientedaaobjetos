import math

def areacuadrado(L):
    return L * L
                    
def areatriangulo(L):
    altura = (math.sqrt(3) / 2) * L
    return (L * altura) / 2
        
def areapentagono(L):
    return L^2 *( L * (math.tan(54 π)) / 4)
    

def perimetro(L, nL):
    return L * nL

while True:
    nL = int(input("Ingresa el numero de lados de la figura: "))
    
    if nL == 1:
        print("No puedo calcular esa figura aun")
    elif nL == 2:
        print("Figura no existente")
    elif  nL == 3:
        L = float(input("Ingresa la medida de los lados de cada figura: "))
        perim = perimetro(L, nL)
        print("-------------------------")
        print(f"Perimetro: {perim}")
        print("-------------------------")
        area = areatriangulo(L)
        print(f"Area: {area:.2f}")
        print("-------------------------")

    elif nL == 4:
        L = float(input("Ingresa la medida de los lados de cada figura: "))
        perim = perimetro(L, nL)
        print("-------------------------")
        print(f"Perimetro: {perim}")
        print("-------------------------")
        area = areacuadrado(L)
        print(f"Area: {area:.2f}")
        print("-------------------------")

    elif nL == 5:
        L = float(input("Ingresa la medida de los lados de cada figura: "))
        perim = perimetro(L, nL)
        print("-------------------------")
        print(f"Perimetro: {perim}")
        print("-------------------------")
        area = areapentagono(L)
        print(f"Area: {area:.2f}")
        print("-------------------------")
        
    else:
        print("-------------------------")
        print("Aun no puedo calcular esa figura")
        print("-------------------------")
