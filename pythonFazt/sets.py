# valores que no tinen un indice

colors = {'Red', 'Green', 'Blue'}
print(type(colors))  # <class 'set'>

print('Red' in colors)

colors.add('Violet')
print(colors)

colors.remove('Violet')
print(colors)

colors.clear()
print(colors)

del colors