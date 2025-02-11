#Crea una clase abstracta Figura con un método abstracto calcular_area(), y luego implementa clases 
# derivadas como Circulo y Rectangulo que calculen su área correspondiente.

from abc import ABC, abstractmethod
import math

# Clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Clases concretas
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

# Uso
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

print(f"Área del círculo: {circulo.calcular_area():.2f}")
print(f"Área del rectángulo: {rectangulo.calcular_area()}")


#Crea una clase CuentaBancaria que tenga atributos privados para el saldo y un método para depositar y retirar dinero, 
# asegurando que el saldo no pueda ser modificado directamente.

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Cantidad inválida para depósito.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def obtener_saldo(self):
        return self.__saldo  # Getter para el saldo

# Uso
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(f"Saldo final: {cuenta.obtener_saldo()}")

#Crea una clase Vehiculo con atributos básicos y dos clases Coche y Moto que hereden de Vehiculo.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        return f"{super().mostrar_info()} con {self.puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()} tipo {self.tipo}"

# Uso
coche = Coche("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR", "deportiva")

print(coche.mostrar_info())
print(moto.mostrar_info())

#Crea una función que reciba diferentes tipos de Figura y calcule sus áreas sin importar su tipo.

def mostrar_area(figura):
    print(f"El área es: {figura.calcular_area()}")

# Uso del polimorfismo
figuras = [Circulo(5), Rectangulo(4, 6)]
for figura in figuras:
    mostrar_area(figura)
