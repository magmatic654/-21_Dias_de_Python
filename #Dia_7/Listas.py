#  Las comprehensions, es una forma de crear listas de una forma más sencilla utilizando una syntaxis compacta.
# Podemos filtrar o transformar elemenentos de una lista existente para crear una nueva lista

# Sintaxis basica

# new_list = [expression for element in original_list if condition]
# expression - define como se transformarán los elementos de la lista original para obtener los elementos de la nueva
# element - es la variabla que representa a cada elemento de la lista original
# original_list - la lista de origen
# condition - condicion que filtra que elementos queremos de la lista original

numbers = [1,2,3,4,5]

# Ejemplos

# Crear una nueva lista con el cuadrado de los números pares de la lista original
even_squared = [number ** 2 for number in numbers if number % 2 == 0]
print(even_squared) # => [4, 16]

# Crear una nueva lista con los números impares multiplicados por 2 de la lista original
odd_multipied = [number * 2 for number in numbers if number % 2 != 0]
print(odd_multipied) # => [2, 6, 10]

# Crear una nueva lista con los números pares de la lista original, y 'No par' para los impares
even_odd = ['Par' if number % 2 == 0 else 'No par' for number in numbers]
print(even_odd)

