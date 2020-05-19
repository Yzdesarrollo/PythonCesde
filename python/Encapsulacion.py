class Ejemplo():

    def publico(self):
        return "Soy un método público, a la vista de todo"
    
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"

objeto = Ejemplo()

print(objeto.publico())

#print(objeto.__privado()) no muestra y sale error

print(objeto._Ejemplo__privado())

"""Metodo get"""
print('----------Metodo get-----------------')

class Ejemplo2():

    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"

    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"
    def get_oculto(self):
        return self.__oculto

objeto = Ejemplo2()

print(objeto.publico())

print(objeto._Ejemplo2__privado())

print(objeto.get_oculto())


"""Metodo set"""
print('----------Metodo set-----------------')

class Ejemplo3():

    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"

    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        print ("Soy un metodo privado, para ti no existo")
    def get_oculto(self):
        return self.__oculto
    def set_oculto(self):
        self.__oculto = self.__privado()

objeto = Ejemplo3()

print(objeto.publico())

print(objeto._Ejemplo3__privado())

print(objeto.get_oculto())

objeto.set_oculto()