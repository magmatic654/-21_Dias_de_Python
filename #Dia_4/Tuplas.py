# tuple
# las tuplas son parecidas a las listas, pero con la
# particularidad de ser inmutables, las tuplas se declaran
# utilizando parentesis
my_tuple = (1,2,3,4,5)

# para acceder a los elementos de las tuplas
# debemos poner el nombre de la tupla y entre
# corchetes poner su indice
coordinates = ((7,2),(1,9),(2,3),(5,1))
print(coordinates[0]) # => (7, 2) 
print(coordinates[0][0]) # => 7 
print(coordinates[0][1]) # => 2 

# como las tulpas con inmutables no es posible modificarlas
# pero encambio si es posible crear una nueva tupla en base
# a la original y con ello agregar elementos en espacios
# determinados.

# Ejemplo
print(coordinates)
new_coordinate = (1,5)
coordinates = coordinates[:1] + (new_coordinate,) + coordinates[1:]
print(coordinates)

# De la misma forma podemos modificar elementos dentro de la tupla
new_coordinate_2 = (8,8)
coordinates = coordinates[:2] + (new_coordinate_2,) + coordinates[2:]
print(coordinates)

########################################################################
# métodos en tuplas

# index - devuelve la primer posición de un elemento buscado
print(coordinates.index((8,8))) # => 8

digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(digits.index(6)) # => 6

# len - retorna la cantidad de elementos de la tupla
print(len(digits)) # => 10

