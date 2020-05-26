
"""Es el ocultamiento de datos del estado interno para
proteger la integridad del objeto
"""

# Encapsulamiento

class Cliente:
    def __init__(self):
        self.__codigo = 4321

    def __cuenta(self):
        print('Cuenta de procesamiento')

    def getcodigo(self):
        return self.__codigo

persona = Cliente()
# objeto._nombreclase__nombre atributo
print(persona._Cliente__codigo)
persona._Cliente__cuenta()

