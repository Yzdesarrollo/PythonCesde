# Strings
"Hello world"
'Hello world'
"""Hello world"""
'''Hello world'''

print(type("Hello world"))  # <class 'str'>

# Numbers
print(type(8))   # <class 'int'>
print(type(4.5)) # <class 'float'>

# Boolean
print(type(False)) # <class 'bool'> False
print(type(True))  # <class 'bool'> True

# List
print(type([10, 20, 30, 40])) # <class 'list'>
['Hello', 'Bye', 'Adios']
[10, 'Hello', True, 10.8]

# Tuples Datos que no cambian
print(type((10, 20, 30, 40))) # <class 'tuple'>

# Dictionary agrupar datos que pertenecen una misma entidad
print(type({'nombre':'Ryan', 'apellido':'Ray', 'apodo':'Fazt'})) # <class 'dict'>

# None
print(type(None)) # <class 'NoneType'>