class Persona:
    edad = 27
    nombre = 'Victor'
    pais = 'brazil'

doctor = Persona()

print('La edad es: ',doctor.edad)
print('La edad es: ', getattr(doctor,'edad'))
print('Existe el atributo?: ',hasattr(doctor,'apellido'))
print('antes: ',doctor.nombre)
setattr(doctor,'nombre','Pedro')
print('despues: ',doctor.nombre)
delattr(Persona,'pais')