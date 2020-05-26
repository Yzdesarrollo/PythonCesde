class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'Estudiante {self.nombre} {self.apellido} {self.edad} años'

nuevo_estudiante = Estudiante('victor', 'cruz', 17)
print(f'{nuevo_estudiante}')


