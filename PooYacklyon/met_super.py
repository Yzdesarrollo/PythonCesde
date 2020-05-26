# Metodo super()

class Mamifero:
    def __init__(self, nombre):
        print(nombre,'Es un animal que se alimenta de leche')

class Leon (Mamifero):
    def __init__(self):
        print('El leon es un animal salvaje')
        super().__init__('Simba')
        # Mamifero.__init__(self, 'SIMBA')

nuevo_leon = Leon()