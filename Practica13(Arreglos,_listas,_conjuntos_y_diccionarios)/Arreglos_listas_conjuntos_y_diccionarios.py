"""
Colecciones
Conjuntos
Diccionario

C = {1,2,3}

"""

c = {1,2,3}
c.add(4)
c.remove(1) #<--- Error si no se encuentra
c.discard(5) #<--- no hay error si no se encuentra
print(1 in c)
print(c)

print("----------------------------------------------------------")
#   Ejercicio: Crear un conjunto de 5 elementos y agregarle un valor, eliminar un valor que existe, eliminar un valor que no existe,
#    agregar un valor existente y verificar existe un valor

c_2 = {"hola mundo", 1.1, 10, "5", 3.14}
print(c_2)
c_2.add("Hola")
print(c_2)
c_2.remove(1.1)
print(c_2)
print("5" in c_2)
c_2.add(10)
print(c_2)
c_2.discard(99)
print(c_2)
#c_2.remove(99)
print("----------------------------------------------------------")
a = {1,2,3}
b = {3,4,5}

u = b|a
#u = b.union(a)
print(u)

i = a&b
#i = b.interseccion(a)
print(i)

d = a-b
#d = a.diference
print(d)

ds = a ^ b
#ds = a.symmetric_difference(b)
print(ds)

print(a.issubset(b))
print(b.issubset(a))
print(a.isdisjoint(b))
print(b.isdisjoint(a))

ac = len(a)
a.clear()
e = a.copy()

