# Propiedades()

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    def __getnombre(self):
        return self.__nombre
    def __getsalario(self):
        return self.__salario

    def __setnombre(self, nombre):
        self.__nombre = nombre
    def __setsalario(self,salario):
        self.__salario = salario

    def __delnombre(self):
        del self.__nombre
    def __delsalario(self):
        del self.__salario

    nombre = property(fget= __getnombre,
                      fset= __setnombre,
                      fdel= __delnombre)

    salario = property(fget= __getsalario)

empleado_uno = Empleado('Hector',3000)
empleado_uno.nombre = 'SARA'
print(empleado_uno.nombre,empleado_uno.salario)
help(empleado_uno)
# empleado_uno = Empleado('victor',2000)
# print(empleado_uno.getnombre(),',',empleado_uno.getsalario())

# empleado_uno.setnombre('Raul')
# print(empleado_uno.getnombre(),',',empleado_uno.getsalario())