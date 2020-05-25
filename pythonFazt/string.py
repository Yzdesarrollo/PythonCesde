myStr = 'Hello world'

# print(dir(myStr)) # Directorio de metodos de python

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'Fazt').upper())
print(myStr.count('l'))
print(myStr.startswith('Hello')) # Si empieza con...
print(myStr.endswith('d'))       # Si termina con...
print(myStr.split('o'))          # Vas a separar a partir de...
print(myStr.find('w'))           # Busca y muestra la posicion de...
print(len(myStr))
print(myStr.index('e'))
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[4])
print(myStr[-1])

# Concatenacion
name = 'Fazt'
print('My name is ' + name)
print(f'My name is {name}')
print('My name is {}'.format(name))
print('My name is {0}'.format(name))
