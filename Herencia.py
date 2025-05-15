from abc import ABC, abstractmethod

class Padres(ABC):
    @abstractmethod
    def rasgos(self):
        pass

class hijo1(Padres):
    def rasgos(self):
        return "color de piel"

class hijo2(Padres):
    def rasgos(self):
        return "color de ojos"

hijo1 = hijo1()
hijo2 = hijo2()

print("hijo1 ", hijo1.rasgos())
print("hijo2 ", hijo2.rasgos())






class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def hacer_sonido(self):
        return "sonido generico"
    
class perro(Animal):
    def hacer_sonido(self):
        return "guau guau"

perrito = perro("Pancho", "Chihuahua") # instancia
print(perrito.nombre)
print(perrito.raza)
print(perrito.hacer_sonido())