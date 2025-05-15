import math
class Figura:
    def perimetro(nl, l):
        if nl == 3:
            return l * 3
        elif nl == 4:
            return l * 4
        elif nl == 5:
            return l * 5
        else:
            return "El calculo de perimetro solo es para triangulos, cuadrados y pentagonos"
        
    def area(nl, l):
        if nl == 4:
            return l * l
        elif nl == 3:
            return (math.sqrt(3)/4) * (l *l)
        elif nl == 5:
            return  (1/4) * (math.sqrt(5*(5 + 2 * math.sqrt(5)))*(l * l))

nl = int(input("Ingresa el numero de lados: "))
l = float(input("Ingresa la longitud de cada lado: "))
perimetro = Figura.perimetro(nl, l)
area = Figura.area(nl, l)
print("El perimetro es", perimetro)
print("El area es", area)      