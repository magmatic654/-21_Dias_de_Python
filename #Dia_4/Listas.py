# Listas
# es un tipo de objeto con el cual se puede almacenar cualquier conjunto
# de tipos de datos como strings, numbers, objects, etc.

# Declaración de una lista
my_list = [True, 'Hola', 40, "Carne"]

primary_colors = ['green', 'red', 'yelow']
print(primary_colors) # => ['green', 'red', 'yelow']

print(primary_colors[0]) # => 'green'
print(primary_colors[1]) # => 'red'
print(primary_colors[2]) # => 'yellow'


digits = [0,1,2,3,4,5,6,7,8,10]
# mutar listas (modificando valores)
# para modificar un valor de una lista en especifico se necesita usar 
# su indice [indice] e igualarlo a otro valor que queramos
digits[-1] = 9 # => 10 -> 9
print(digits) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Métodos más usados en las listas

# append
# Agrega un elemento dentro de la lista al final de la misma
students = ['jose', 'harold', 'matias', 'andres', 'ximena']
# añadir nuevo elemento al final de la lista
students.append('carmen')
print(students) # => ['jose', 'harold', 'matias', 'andres', 'ximena', 'carmen']

# pop
# Elimina por defecto el ultimo elemento de la lista, también se
# le puede pasar un elemento en especifico por su indice
# Por defecto
students.pop()
print(students) # => ['jose', 'harold', 'matias', 'andres', 'ximena']
# Con indice
students.pop(0)
print(students) # => ['harold', 'matias', 'andres', 'ximena']

# count
# cuenta las veces que un elemento estña en la lista, solo le debemos pasar 
# el elemento que queremos contar.
random_numbers = [1, 6, 8, 3, 2, 1, 6, 9, 3, 3, 2]
print(random_numbers.count(3)) # => 3 
print(random_numbers.count(1)) # => 2 
print(random_numbers.count(9)) # => 1 
# contar el número de jose de un grupo
group_names = ['jose', 'fernando', 'jose', 'alfonso', 'erick', 'jose']
print(group_names.count('jose')) # => 3

# reverse
# invirte el sentido de la lista acomodando los elementos de la misma al revez
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers) # => [5, 4, 3, 2, 1]

# sort
# ordena los números de manera ascendente o descendente
numbers = [10,2,3,23,2,6,32,5,2,6,1,2,4,9,14]
# ascendente
numbers.sort()
print(numbers) # => [1, 2, 2, 2, 2, 3, 4, 5, 6, 6, 9, 10, 14, 23, 32]
# descendente
numbers.sort(reverse=True)
print(numbers) # => [32, 23, 14, 10, 9, 6, 6, 5, 4, 3, 2, 2, 2, 2, 1]

