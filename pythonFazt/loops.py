print('-------------FOR----------------')


foods = ['apples', 'bread', 'cheese', 'milk', 'bananas', 'graves']

for food in foods:
    if food == 'cheese':
        print('tienes que comprar esto')
        continue
    print(food)

for number in range(1, 8):
    print(number)

for letra in 'Hello':
    print(letra)


print('-------------WHILE----------------')

count = 4

while count <= 10:
    print(count)
    count = count + 1