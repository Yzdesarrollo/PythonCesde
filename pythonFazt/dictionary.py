product = {'name': 'book', 'cantidad':3, 'precio': 4.99}
print(type(product))
print(dir(product))

person = {'firts_name' : 'ryan', 'last_name' : 'ray'}
print(type(person))
print(dir(person))

print(person.keys()) # Obtiene los valores de las llaves
print(person.items()) # Obtiene los valores de los items

# del person

person.clear()
print(person)

products = [{'name':'book', 'price':10.99},{'name':'laptop', 'price':1000}]
print(products)