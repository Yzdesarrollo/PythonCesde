
class Contador():

    inicio = 0

    def empezar(self):
        print('Inicia conteo')

class Comienzo():

    inicio = 1

    def arranque(self):
        print('Arranca el conteo en 1')

print('-----------------Primer Objeto-------------------------')

conteo=Contador()

print('Conteo iniciara en', conteo.inicio, 'para empezar')

conteo.empezar()

print('-----------------Segundo Objeto------------------------')

conteo2=Comienzo()

print('Se ha iniciado el conteo en', conteo2.inicio, 'para el recorrido')

conteo2.arranque()