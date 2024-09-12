# Queues o Cola
# Una Queue es una estructura de datos final que aplica el principio de FIFO (First In, First Out), lo que quiere decir que el primer elemento en este tipo de estructuras es el primero en ser eliminado, parecido a lo que pasa en una fila en la vida real

# Complejidad Algoritmica
# Los metodos de cola tienen una complejidad algoritmica constante, por lo que su eficiencia no depende del tama;o de la cola
# Acceder a elementos - O(n)
# Insertar - O(1)
# Eliminar - O(1)
# Verificar si esta vavia O(1)
# Verificar la cantidad O(1)

# Oportunidades para utilizar Queue
# 1. Procesamiento en el mismo orden de llegada (mensajes de correo electronico, solicitudes de clientes, tareas en un sistema de planificacion, etc)
# 2. Registro de eventos (ultimos elemmentos agregados o modificados, como registros de transacciones en un sistema de bases de datos
# 3. Recorrido de amplitud (BFS): En algoritmos de busqueda en arboles o grafos, como el recorrido en amplitud(BFS), donde se deben explorar los nodos en el orden de proximidad desde un nodo inicial)

# Situaciones donde no es conveniente utilizarlos
# Acceso aleatorio o elementos por indice (Es mas conveniente utilizar arrays o listas enlazadas)
# Busqueda de elementos especificos (es mas conveniente utilizar un hash table (diccionario))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise IndexError('la queue esta vacia')
        removed_node = self.first
        if self.length == 1:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return removed_node
    
    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length