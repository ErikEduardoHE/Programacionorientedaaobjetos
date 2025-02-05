import math

class Figura:
    
    def cuadrado(self, L):
        return L * L
                    
    def triangulo(self, L):
        altura = (math.sqrt(3) / 2) * L
        return (L * altura) / 2
            
    def figurasregulares(self, L, nL):
        angulo_radianes = (math.pi / nL)
        return (nL * L**2) / (4 * math.tan(angulo_radianes))

    def perimetro(self, L, nL):
        return L * nL

figura = Figura()

while True:
    nL = int(input("Ingresa el numero de lados de la figura: "))
    
    if nL == 1:
        print("No puedo calcular esa figura aún.")
   
    elif nL == 2:
        print("Figura no existente.")
   
    elif nL >= 3:
        L = float(input("Ingresa la medida de los lados de la figura: "))
        perim = figura.perimetro(L, nL) 
        print("-------------------------")
        print(f"Perímetro: {perim}")
        print("-------------------------")
        area = figura.figurasregulares(L, nL) 
        print(f"Área: {area:.2f}")
        print("-------------------------")
        
    else:
        print("-------------------------")
        print("Aún no puedo calcular esa figura.")
        print("-------------------------")
