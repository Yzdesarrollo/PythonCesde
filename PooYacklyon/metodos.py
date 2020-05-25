""" CLASE nombre de la clase:
        DEF nombre del metodo (SELF):
    SELF.nombre de la variable = ALGORITMO ó VALOR"""

class Matematica:
    def sumar(self):
        self.n1 = 2
        self.n2 = 3

ej = Matematica()
ej.sumar()
print(ej.n1 + ej.n2)

""" CONSTRUCTOR """

class Ropa:
    def __init__(self):
        self.marca = 'Nike'
        self.talla = 'M'
        self.color = 'rojo'

camisa = Ropa()
print(camisa.marca)
print(camisa.talla)
print(camisa.color)

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(5, 8)
print(operacion.suma)


class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre,self.año)
    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre,frase)

doctor = Persona('Jose', 26)
print(doctor.descripcion())
print(doctor.comentario('Hola que tal'))


class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)