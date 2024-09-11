# Singly Linked List
# Una lista enlazada simple es una estructura de datos lineal en la que cada elemento (nodo) contiene un valor y un puntero que apunta hacia el siguiente nodo de la lista. 
# La lista enlazada empieza con un nodo llamado head que apunta al primer elemento de la lista, y termina con un nodo de la cola (tail) que apunta a None

# Complejidad algoritmica
# Acceder a Elementos O(n)
# Insercion al Inicio O(1)
# Insercion al Final O(n)
# Insercion en Medio O(n)
# Eliminacion al Inicio O(1)
# Eliminacion al Final O(n)
# Eliminacion en Medio O(n)

# Ventajas
# - Espacio en memoria
# Incercion y Eliminacion O(1) al inicio de la lista
# Tamaño dinamico de la lista

# Desventajas
# Acceder a la posicion n de un elemento requiere tiempo linal O(n)
# Solo tienen recorrido hacia adelante y no para atras
# No sirven muy bien para operaciones de busqueda frecuentes por complejidad O(n)



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.head = self.head
            self.head = new_node
        self.length += 1

    def delete(self, value):
        if self.head == None:
            return
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                self.length -= 1
                return 
            current_node = current_node.next
