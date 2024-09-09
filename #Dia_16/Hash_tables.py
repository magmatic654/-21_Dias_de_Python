# Hash tables en Python

# Las hash tables, también conocidas como tablas hash o diccionarios, son estructuras de datos eficientes y versátiles que nos permiten almacenar y recuperar datos utilizando una función hash.

# La idea principal detrás de las hash tables es utilizar una función hash para calcular el índice donde se almacenará cada par clave-valor en un arreglo de tamaño fijo. La función hash toma la clave y produce un valor numérico único que se utiliza para determinar la ubicación en la tabla. Esto permite un acceso rápido a los valores, ya que no es necesario buscar a través de todos los elementos como en una lista o una matriz.

# Complejidad algorítmica
# Si medimos la complejidad de los métodos de la hash table con Big o notation, podremos notar que es de lo más eficiente. Debido a que siempre se mantiene constante.

# Operación	Complejidad Algorítmica
# Inserción	O(1)
# Búsqueda	O(1)
# Eliminación	O(1)
# En una hash table bien implementada con una función hash eficiente, todas estas operaciones tienen una complejidad constante (O(1)). Esto significa que el tiempo de ejecución no depende del tamaño de la hash table, lo cual es una característica clave de las hash tables y las hace altamente eficientes para manejar grandes volúmenes de datos.

# Implementación básica de una hash table
# En python basta con usar un simple diccionario como hash table o crear tu propia implementación como verás a continuación

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.buckets = [[] for _ in range(size)]

#     def hash(self, key):
#         La función hash toma una clave y devuelve un índice calculado
#         utilizando una función hash.
#         return hash(key) % self.size

#     def insert(self, key, value):
#         El método insert toma una clave y un valor, 
# 				y los almacena en la hash table.
#         index = self.hash(key)
#         self.buckets[index].append((key, value))

#     def get(self, key):
#         El método get toma una clave 
# 				y devuelve el valor correspondiente almacenado en la hash table.
#         index = self.hash(key)
#         for k, v in self.buckets[index]:
#             if k == key:
#                 return v
#         return None

#     def remove(self, key):
#         El método remove toma una clave
# 				 y elimina el par clave-valor correspondiente de la hash table.
#         index = self.hash(key)
#         for i, (k, v) in enumerate(self.buckets[index]):
#             if k == key:
#                 del self.buckets[index][i]
#                 return

#     def retrieve_all(self):
#         El método retrieve_all devuelve todos 
# 				los valores almacenados en la hash table.
#         all_values = []
#         for bucket in self.buckets:
#             for key, value in bucket:
#                 all_values.append(value)
#         return all_values

# Esta implementación utiliza una lista de listas (self.buckets) para representar los buckets de la hash table. Cada bucket es una lista que almacena los pares clave-valor correspondientes. La función hash se implementa utilizando la función hash() incorporada de Python, y se utiliza el operador módulo (%) para asegurar que el índice calculado esté dentro del rango válido de buckets.

# Los métodos insert, get, remove y retrieve_all proporcionan la funcionalidad básica para manipular la hash table. Puedes utilizar estos métodos para insertar pares clave-valor, obtener valores por clave, eliminar pares y obtener todos los valores almacenados.

# Al comprender y utilizar las hash tables de manera efectiva, podemos optimizar el rendimiento y resolver problemas de manera eficiente en una amplia gama de aplicaciones.