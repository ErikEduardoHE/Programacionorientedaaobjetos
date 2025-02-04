import math

def cuadrado(L):
    return L * L
                    
def triangulo(L):
    altura = (math.sqrt(3) / 2) * L
    return (L * altura) / 2
        
def figurasregulares(L):
    angulo_radianes = (math.pi / nL)
    return nL * L**2 / 4 * math.tan(angulo_radianes)

def perimetro(L, nL):
    return L * nL

while True:
    nL = int(input("Ingresa el numero de lados de la figura: "))
    
    if nL == 1:
        print("No puedo calcular esa figura aun")
   
    elif nL == 2:
        print("Figura no existente")
   
    elif nL >= 3:
        L = float(input("Ingresa la medida de los lados de cada figura: "))
        perim = perimetro(L, nL)
        print("-------------------------")
        print(f"Perimetro: {perim}")
        print("-------------------------")
        area = figurasregulares(L)
        print(f"Area: {area:.2f}")
        print("-------------------------")
        
    else:
        print("-------------------------")
        print("Aun no puedo calcular esa figura")
        print("-------------------------")
