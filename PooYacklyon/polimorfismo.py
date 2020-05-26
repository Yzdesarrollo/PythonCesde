"""Es la capacidad que tienen 
los objetos en diferentes clases para usar un comportamiento
o atributo del mismo nombre pero con diferente valor"""

# POLIMORFISMO - HERENCIA

# class Auto:
#     rueda = 4
#     def desplazamiento(self):
#         print('El auto se esta desplazando')

# class Moto:
#     rueda = 2
#     def desplazamiento(self):
#         print('El auto se esta desplazando')

class Aves:
    def volar(self):
        print('La mayoria de las aves pueden volar pero otras no')

class Aguila(Aves):
    def volar(self):
        print('Las Aguilas pueden volar alto')

class Gallina(Aves):
    def volar(self):
        print('Las gallinas no puede volar')

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()

obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()



class Animales:
    def __init__(self,nombre):
        self.nombre = nombre
    def tipo_animal(self):
        pass
class Leon(Animales):
    def tipo_animal(self):
        print('animal salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print('animal domestico')

nuevo_animal = Leon('SIMBA')
nuevo_animal.tipo_animal()

nuevo_animal = Perro('REX')
nuevo_animal.tipo_animal()

# POLIMORFISMO POR FUNCION

class Tomate:
    def tipo(self):
        print('vegetal')
    def color(self):
        print('rojo')

class Manzana:
    def tipo(self):
        print('fruta')
    def color(self):
        print('verde')

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate)

nuevo_manzana = Manzana()
funcion(nuevo_manzana)

# POLIMORFISMO CON METODOS

class Colombia:
    def capital(self):
        print('Bogota')
    def idioma(self):
        print('español')

class Francia:
    def capital(self):
        print('Paris')
    def idioma(self):
        print('frances')

colombiano = Colombia()
frances = Francia()

for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()


