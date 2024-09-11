# stacks o pilas
# Los stacks son estucturas de datos lineal, la cual se rige por el principio de Ultimo en entrar, primero en salir (LIFO - Last In, First Out)

# Complejidad algoritmica
# Agregar un elemento - O(1)
# Eliminar un elemento - O(1)
# Acceder al ultimo elemento - O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0
    
    def push(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.lenght += 1
    
    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        popped_node = self.top
        self.top = self.top.next
        self.lenght -= 1
        return popped_node.value
    
    def peek(self):
        return self.top.value if self.top else None
    
    def is_empty(self):
        return self.lenght == 0