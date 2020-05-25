class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
         return '{} es un pokemon de tipo: {} '.format(self.nombre, self.tipo)

class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipo_ataque)

class Charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipo_ataque)

nuevo_pokemon = Pikachu('Pikachu', 'electrico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('impacto trueno'))

nuevo_pokemon = Charmander('Charmander', 'fuego')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('remolino de fuego'))


# EJERCICIO PRACTICO

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresar_dato(self):
        self.datos = [int(input('Ingrear datos ' + str(i+1) + ' = ')) for i in range(self.n)]

class operaciones(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
            a,b, = self.datos
            s = a + b
            print('El resultado es: ', s)

    def resta(self):
            a,b, = self.datos
            r = a - b
            print('El resultado es: ', r)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a, = self.datos
        print('El resultado es: ', math.sqrt(a))

# ejemplo = operaciones()
# print(ejemplo.ingresar_dato())
# print(ejemplo.suma())

# ejemplo = raiz()
# print(ejemplo.ingresar_dato())
# print(ejemplo.cuadrada())

objeto = operaciones()

"""Funciones integradas"""
print(isinstance(objeto,raiz))
print(issubclass(operaciones,Calculadora)) # si la clase hijo pertenece a la clase padre

