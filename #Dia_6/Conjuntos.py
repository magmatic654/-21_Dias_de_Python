# sets
# Son estructuras de datos sin orden que guardan valores 
# unicos sin repetir ninguno de ellos.

# Crear un set
my_set_1 = set()

# Crear set a partir de una lista existente
my_list_1 = [1,2,3,4,5]
my_set_2 = set(my_list_1)
print(my_set_2) # => {1, 2, 3, 4, 5}

###############################################################
# Métodos de sets

# add(value) 
# agrega un valor unico al set, si este valor  ya existe en el 
# set, entonces no se agregará

# remove(value)
# Elimina un valor en especifico del set, si no existe, se 
# generará un error

# discard(value)
# Elimina un valor en especifico del set, si no existe, no
# generará ningún error

# pop()
# Elimina y retorna un valor aleatorio del set

# clear()
# Vacía completamente el set

# len()
# retorna el tamaño del set (cantidad de elementos que hay en el)

# Ejemplos

# add
my_set_1.add(1)
my_set_1.add('dos')
my_set_1.add(3)
my_set_1.add('cuatro')
print(my_set_1) # => {3, 1, 'dos', 'cuatro'}

# verificar si un elemento existe en el set
print('dos' in my_set_1) # => True
print(2 in my_set_1) # => False

# remove
my_set_1.remove('dos')
print(my_set_1) # =Z {1, 3, 'cuatro'}

# discard
my_set_1.discard(3)
print(my_set_1) # =Z {1, 'cuatro'}

# len 
len_my_set = len(my_set_1)
print(len_my_set) # => 2

# clear
my_set_1.clear()
print(my_set_1) # => set()

# len
print(len(my_set_1)) # => 0

#####################################################
# Iterar en sets

# for in
my_set_3 = {1,2,3,4,5}
for element in my_set_3:
    print(element) # => 1, # => 2, # => 3, # => 4, # => 5

# Pasar a lista para utilizar slice
my_set_3 = list(my_set_3)
# slice syntax
for element in my_set_3[1:]: # => inicia desde la posición uno hasta la ultima
    print(element) # => 2, # => 3, # => 4, # => 5

for element in my_set_3[3:]: # => inicia desde la posición tres hasta la ultima
    print(element) # => 4, # => 5

for element in my_set_3[3:4]: # => inicia desde la posición tres hasta la cuarta
    print(element) # => 4

for element in my_set_3[::-1]: # => inicia desde la ultima posicion hasta la primera
    print(element) # => 5, # => 4, # => 3, # => 2, # => 1

# volver a set
my_set_3 = set(my_set_3)
##########################################################
# Intersecciones
# la interseccion es una operacion en la que se comprueba que elementos
# existen en dos o más conjuntos a la vez, se puede hacer con 
# intersection() o el operador &

set_1 = {1, 2, 4, 6, 8, 10}
set_2 = {2, 3, 5, 7, 8, 9}

# intersection
print(set_1.intersection(set_2)) # => {8, 2}

# &
print(set_1 & set_2) # => {8, 2}