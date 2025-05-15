class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

def escuchar_animal(animal: Animal):
    print(animal.hacer_sonido())

mi_perro = Perro()
mi_gato = Gato()

print(escuchar_animal(mi_perro))
print(escuchar_animal(mi_gato))