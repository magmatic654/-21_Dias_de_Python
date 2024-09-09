# Las estructuras de datos proporcionan un medio eficiente y accesible para organizar y almacenar datos.
# En python existen estructuras nativas y personalizadas
# las estructuras más comunes y poderosas son: listas, tuplas, conjuntos, diccionarios, pilas, colas, árboles y grafos.

# Estructuras Nativas

# Listas
# Es una secuencia ordenada y mutable de elementos. Pueden contener distintos tipos de datos y se permite la modificacion de los elementos individuales. 
# las listas se definen utilizando corchetes [] y los elementos separados por comas
my_list = [1, 2, 3, 'Hola', True]

# Tuplas
# Las tuplas son similares a las listas, pero son inmutables, lo que significa que una vez creadas no pueden ser modificadas.
# Las tuplas se definen con parentesis () y los elementos se separan por comas
my_tuple = (1, 2, 3, 'Hola', True)

# Conjuntos
# Un conjunto es una coleccion no ordenada de elementos unicos mutablesm, esto significa que en un conjunto no permite elementos duplicados y se utiliza principalmente para realizar operaciones de conjuntos, como interserccion, union, interseccion y diferencia
# Los conjuntos se definen utilizando llaves {} o la función set()
my_set = {1, 2, 3, 4, 5}

# Diccionarios
# Los diccionarios son estructuras de datos que almacenan pares clave-valor
# Cada elemento del diccionario se compone de una clave y un valor, para acceder al valor de un elemento de un diccionario se necesita el nombre de la clave.
# Los diccionarios se definen utilizando llaves {} y los pares clave-valor se separan por comas.
my_dict = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}

# Estructuras de datos que pueden ser implementadas 
#########################################################

# Pilas
# Una pila es una estructura de datos lineal que sigue la regla LIFO (Last In, First Out), lo que significa que el último elemento agregado es el primero en ser retirado.
# Las pilas se utilizan en situaciones donde es necesario llevar un seguimiento de elementos y realizar operaciones como agregar y quitar elementos en el extremo superior de la pila.

# Colas
# Una cola es similar a una pila, pero sigue la regla FIFO (Last In, First Out), lo que significa que el primer el primer elemento agregado es el primero en ser retirado.
# Las colas se utilizan para modelar situacionesa en las que es necesario procesar elementos en el mismo orden en el que se agregaron, como en la gestion de tareas
 
# Arboles
# Es una estructura de datos no lineal compuesta por nodos conectados mediante enlaces llamados bordes o aristas.
# Cada nodo puede tener cero o más hijo y se define un nodo especial llamado raíz que es el punto de partida del árbol.
# Los arboles se utilizan para representar estructuras jerarquicas y se aplican a problemas como la organizacion de archivos, la representacion de árboles genealógicos y la optimizacion de algoritmos de búsqueda.

# Grafos
# Un grafo es una estructura de datos que consta de un conjunto de nodos (tambien llamados vértices) y un conjunto de conexiones entre ellos (también llamados aristas).
# Los grafos se utilizan para representar relaciones complejas entre entidades y se aplican en problemas como la navegacion de mapas, el análisis de redes sociales y la optimizacion de rutas

 