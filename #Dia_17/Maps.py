# Los maps en python son estructuras de datos que permiten almacenar pares claves-valor y acceder a ellos de manera eficiente.
# Las claves de un map pueden ser cualquier tipo de dato inmutable incluyendo enteros, cadenas, tuplas, y objetos personalizados.
# Los Maps son utiles cuando se necesitan hacer busquedas rapidas de valores asociados a una clave determinada

my_map = {}

pairs = [('key1', 'value1'),('key2', 'value2')]
map = dict(pairs)

print(map)
# Metodos mas utilizados de los Maps:

# map[key] = value: Este metodo agrega un par clave-valor al Map

# value = map.get(key): Este metodo devuelve el valor asociado a una clave determinada, si la clave no existe devuelve None

# key in map: Este metodo verifica si una clave determinada existe en el Map. Devuelve True si la clave existe y False en caso contrario

# del Map[key]: Este metodo elimina una clave y su valor asociado del Map

# map.clear(): Este metodo vacia completamente el Map

# len(map) : Esta funcion devuelve la cantidad de pares clave-valor que hay en el Map

map = {}
# Agregar un par clave valor al Map
map['key1'] = 'value1'
map['key2'] = 'value2'
map[3] = 'value3'

# Obtener el valor asociado a una clave
print(map.get('key1')) # => 'value1'  

# Verificar si una clave existe en el Map
print('key2' in map) # => True

# Eliminar una clave-valor del Map
del map['key2']

# Verificar si una clave existe despues de ser eliminada
print('key2' in map) # => False

# Vaciar el Map
map.clear()

# Verificar la longitud del Map despues de ser vaciado
print(len(map)) # => 0