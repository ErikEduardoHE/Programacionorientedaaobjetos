class Biblioteca:
    def __init__(self):
        self._libros = []

    def agregar_libro(self, titulo):
        self._libros.append(titulo)
        print("Libro",{titulo}, "agregado a la biblioteca")

    def eliminar_libro(self, titulo):
        if titulo in self._libros:
            self._libros.remove(titulo)
            print("Libro",{titulo}, "eliminado de la biblioteca")
        else:
            print("El libro", {titulo}, "no se encuentra en la biblioteca")

    def mostrar_libros(self):
        if self._libros:
            print("Libros en la biblioteca:")
            for libro in self._libros:
                print("-", {libro})
        else:
            print("La biblioteca esta vacia")

mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_libro("Cien años de soledad")
mi_biblioteca.agregar_libro("Don Quijote de la Mancha")
mi_biblioteca.mostrar_libros()
mi_biblioteca.eliminar_libro("Cien años de soledad")
mi_biblioteca.mostrar_libros()