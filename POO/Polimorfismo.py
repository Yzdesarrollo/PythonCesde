"""Metodo construtor"""
print('----------Metodo Constructor-------------')
class Perro():
    def __init__(self, color, raza):
        self.color = color
        self.raza  = raza

Tobby = Perro('Negro', 'Bull Terry')

print('Tobby es un perro de raza {} y es de color {}'.format(Tobby.raza, Tobby.color))

"""Metodo string"""
print('----------Metodo string"-----------------')
class Perro2():

    def __init__(self, color, raza):
        self.color = color
        self.raza = raza

    def __str__(self):
        return """\
Raza: {}
Color: {}""".format(self.raza, self.color)


Kaizer = Perro2("Marrón claro", "Golden retriever")

print(Kaizer)

"""Metodo repr"""
print('----------Metodo repr"-----------------')

class Cachorro():

    def __init__(self, color, raza, id):
        self.color = color
        self.raza = raza
        self.id = id

    def __str__(self):
        return """ Raza: {} Color: {}""".format(self.raza, self.color)

    def __repr__(self) -> str:
        return "<Cachorro {}>".format(self.id)


perrito = Cachorro("Marrón claro", "Golden retriever", 1)
print(repr(perrito))
