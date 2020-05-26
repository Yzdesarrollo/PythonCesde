"""
Metodos estaricos 
Metodos estaticos 
Metodos de instancia
"""


# Metodo de Clase
print('--------------METODO DE CLASE-----------------')
# class Pastel:
#     def __init__(self,ingredientes):
#         self.ingredientes = ingredientes

#     def __repr__(self):
#         return f'Pastel({self.ingredientes !r})'

#     @classmethod
#     def Pastel_chocolate(cls):
#         return cls(['harina', 'leche', 'chocolate'])

#     @classmethod
#     def Pastel_vanilla(cls):
#         return cls(['harina','leche', 'vainilla'])

# print(Pastel.Pastel_chocolate())

# Metodo Estatico
print('--------------METODO ESTÁTICO-----------------')
import math
class Pastel:
    def __init__(self,ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    def __repr__(self):
        return (f'Pastel ({self.ingredientes}, 'f'{self.tamaño})')
    def area(self):
        return self.tamaño_area(self.tamaño)

    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi

nuevo_pastel = Pastel(['harina', 'azucar', 'leche', 'crema'], 4)
print(nuevo_pastel.ingredientes)
# print(nuevo_pastel.tamaño)
print(nuevo_pastel.tamaño_area(12))

