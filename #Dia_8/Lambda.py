# las funciones lambda son funciones anónimas que pueden escribirse en una sola linea de codigo, se utilizan para realizar operaciones simples y rapidas.

# sintaxis basica
# lambda arguments: expression

# arguments - son los parametros de la función
# expression - la operacion que se realizará y retornará

#############################################################
# funciones con lambdas, comunmente se utilizan las funciones lambda en
# conjunto con otras, como map(), filter() y reduce(), para realizar operaciones sobre secuencias

# Ejemplos

# lambda simple
suma = lambda a, b: a + b
result = suma(2, 5) 
print(result) # => 7

# lambda con map()
numbers = [1, 2, 3, 4, 5]
duplicades = list(map(lambda x: x * 2, numbers))
print(duplicades) # => [2, 4, 6, 8, 10]

# lambda con filter()
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even) # => [2, 4]

