print('-----------FUNCION-----------------------------')
def hello(name='Persona'):
    print(f'Hello {name}')

hello('Fazt')
hello('Ryan')
hello()

print('-----------FUNCION CON RETURN-----------------')
def add(num1, num2):
    return num1 + num2

print(add(10, 20))
print(add(600, 20))

print('-----------FUNCION LAMBDA O ANÓNIMA----------')
add1 = lambda numberOne, numberTwo: numberOne + numberTwo
print(add1(80, 20))
