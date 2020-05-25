# Clases

class Carro:
    marca = ''
    modelo = 0
    placa = ''

taxi = Carro()
print(taxi.modelo)

class Persona:
    name = 'Yeison'

print(Persona.name)

class Jugadores:
    j1 = 'Messi'
    j2 = 'Cristiano Ronaldo'

print(Jugadores.j1)

class Nombre:
    pass

victor = Nombre()
Maria  = Nombre()

# objeto.atributo = valor

victor.edad = 30
Maria.edad = 25

print(victor.edad)
print(Maria.edad)