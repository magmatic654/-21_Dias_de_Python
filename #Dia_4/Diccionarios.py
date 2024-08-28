# dict
# Los diccionarios permiten almacenar conjuntos pares 
# de clave-valor key-value
my_dict = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3'
}

# Ejemplo
classroom = {
    'group': 'a',
    'students': [
        {'name': 'harold', 'age': 30, 'faults': 0},
        {'name': 'fernando', 'age': 20, 'faults': 4},
        {'name': 'joel', 'age': 35, 'faults': 5},
        {'name': 'marta', 'age': 33, 'faults': 1},
        {'name': 'bruno', 'age': 25, 'faults': 0},
    ],
    'professor': 'Vladimir Andres Fuentes Cruz' ,
    'reports': 0
}

# Para acceder a los valores dentro del diccionario 
# hace falta una notacion con corchetes y pasar la key 
# que buscamos y con ello retornara el value
print(classroom['students']) # imprime todos los estudiantes
print(classroom['professor'])   # => 'Vladimir Andres Fuentes Cruz'

# Los diccionarios pueden contener métodos

# Ejemplo #1
basic_operations = {
    'sum': lambda a, b: print(a+b),
    'sub': lambda a, b: print(a-b),
    'mul': lambda a, b: print(a*b),
    'div': lambda a, b: print(a/b)
}

basic_operations['sum'](1,2)
basic_operations['sub'](10,5)
basic_operations['mul'](9,4)
basic_operations['div'](16,2)

# Ejemplo #2
car = {
    'brand': 'Toyota',
    'start_engine': lambda: print('El coche ha sido encendido')
}

car['start_engine']()