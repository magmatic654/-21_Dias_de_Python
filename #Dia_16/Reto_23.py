# Tu objetivo es crear una clase llamada MyList que simule el comportamiento de una Lista nativa en Python, sin utilizar los métodos ya existentes. Implementarás la lógica de los siguientes métodos:

# map(func): itera sobre cada elemento de nuestra estructura aplicando la función func a cada uno de ellos y devuelve una nueva lista (que será una instancia de MyList).

# filter(func): itera sobre cada elemento de nuestra estructura filtrándolos según lo que indique la función func y devuelve una lista con los elementos filtrados (también una instancia de MyList).

# join(character): concatena todos los elementos de nuestra estructura de datos en un string, separándolos por el carácter indicado (character). Si no se proporciona un carácter, el separador por defecto será una coma ",".

# append(item): agrega un elemento item al final de la lista y aumenta la longitud (length).

# pop(): elimina el último elemento de la lista y lo retorna, disminuyendo también la longitud (length).

# shift(): elimina el primer elemento de la lista y lo retorna, disminuyendo la longitud (length).

# unshift(item): agrega un elemento item al inicio de la lista y aumenta la longitud (length).

# Además, deberás almacenar los elementos dentro de la propiedad data y el número de elementos dentro de la propiedad length, para que puedan ser consultados desde las pruebas.

# Ejemplo 1:

# Input:
# myList = MyList()
# myList.append("a")
# myList.append("b")
# myList.append("c")
# print(myList.data)

# Output:
# {0: 1, 1: 2, 2: 3}

# Ejemplo 2:

# Input:
# myList = MyList()
# myList.append("Platzinauta")
# myList.unshift("Hola!")
# print(myArray.data)

# Output:
# {0: "Hola!", 1: "Platzinauta"}

class MyList:
    def __init__(self, data = {}, length = 0):
        self.data = data
        self.length = length

    def map(self, func):
        return MyList({key: func(value) for key, value in self.data.items()}, self.length)

    
    def filter(self, func):
        # new_list = MyList(: value for key, value in self.data.items() if func(value)})
        new_list = {}
        counter = 0
        for i in range(self.length):
            if func(self.data[i]):
                new_list[counter] = self.data[i]
                counter += 1
        return MyList(new_list, counter)
    
    def join(self, character = ','):
        new_string = ''
        for item in self.data.values():
            new_string += str(item) + str(character)
        new_string = new_string[:-3]
        return new_string

    def append(self, item):
        self.add(self.length, item)
    
    def pop(self):
        return self.delete(self.length - 1)
    
    def shift(self):
        return self.delete(0)

    def unshift(self, item):
        self.add(0, item)
        
    def delete(self, index):
        if self.length <= 0:
            raise Exception('No hay elementos dentro de la lista')
        
        if index >= self.length or index < 0:
            raise IndexError('Índice fuera de rango')
        
        # Crear un nuevo diccionario temporal para reasignar las llaves
        dict_temp = {}
        counter = 0
        item = self.data[index]
        # Reorganizar los elementos anteriores al índice a eliminar
        for i in range(0, index):
            dict_temp[counter] = self.data[i]
            counter += 1
        
        # Reorganizar los elementos posteriores al índice eliminado
        for i in range(index + 1, self.length):
            dict_temp[counter] = self.data[i]
            counter += 1
        
        self.data = dict_temp
        self.length -= 1
        return item
    
    def add(self, index, item):
        self.data[index] = item
        self.length += 1



myList = MyList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
# print(myList.data)
# myList.append("Platzinauta")
# myList.unshift("Hola!")
# print(myList.data)
# print(myList.data)
# double = lambda x: x*2
# print(myList.map(double).data)
# print(myList.map(double).length)

# even = lambda x: x % 2 == 0
# print(myList.filter(even).data)
# print(myList.filter(even).length)

# print(myList.pop())
print(myList.join())