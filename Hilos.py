import threading
from time import sleep

class hilo(threading.Thread):
    def __init__(self, nombre, intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo

    def run(self):
        print(f"El hilo {self.nombre} ha comenzado")
        for i in range(5):
            print(F"El hilo {self.nombre} se encuentra en iteracion {i}")
            sleep(self.intervalo)
        print(f"El hilo {self.nombre} ha finalizado")

hilo1 = hilo("hilo_1", 2)
hilo2 = hilo("hilo_2", 4)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()