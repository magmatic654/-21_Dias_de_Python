# Los dictionary comprehensions permiten una rapida y eficiente creacion de diccionarios utilizando una syntaxis compacta y elegante.
# Permiten transformar y filtrar elementos de una secuencia para crear un diccionario completamente nuevo

# sintaxis basica
# my_dict = {key_expression: value_expression for element in sequence if condition}

# key_expression - define que nombre le daremos a la clave del diccionario
# value_expression - define que nombre le daremos al valor del diccionario
# element - los elementos de la secuencia
# sequence - la secuencia de origen
# condition - la condicion opcional para que la clave-valor sean agregados al diccionario

# Ejemplos
people = [("Juan", 25), ("María", 30), ("Pedro", 20)]

# Crear un nuevo diccionario con el nombre como clave y la edad como valor, solo para personas mayores de 25 años
up_25years = {name: age for (name, age) in people if age >= 25}
print(up_25years)

# Crear un nuevo diccionario con el nombre como clave y la longitud del nombre como valor para todas las personas
length_names = {name: len(name) for (name, age) in people}
print(length_names)

