demo_list = [1, 'hello', 1.34, True, [1, 2, 3]] 
colors = ['red', 'green', 'blue']

numbers_list = list((1,2,3))
print(type(numbers_list))

r = list(range(1, 11)) # del 1 al 10
print(r)

print(type(colors))
# print(dir(colors))
print(len(colors))
print(len(demo_list))
print(colors[1])
print(colors[-1])
print('green' in colors)


print(colors)
colors[1] = 'yellow'
print(colors)

colors.append('violet')
print(colors)

colors.extend(['brown', 'white'])
print(colors)

colors.extend(('pink', 'black'))
print(colors)

colors.insert(1, 'black') # Poner el elemento en una posision especifica
print(colors)

colors.insert(len(colors), 'golden') # Poner el elemento teniendo encuenta la longitud de la lista
print(colors)

colors.pop() # Quitar un elemento de la lista
print(colors)

colors.remove('black')
print(colors)

colors.remove('black')
print(colors)

# colors.clear()
# print(colors)

colors.sort() # Ordenarlos alfabeticamente
print(colors)


colors.sort(reverse=True) # Ordenarlos alfabeticamente de manera inversa
print(colors)

print(colors.index('yellow'))

print(colors.count('yellow')) # Cuantas veces existe
