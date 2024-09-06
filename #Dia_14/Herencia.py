# Herencia
# Permite crear nuevas clases a partir de clases ya existentes heredando sus métodos y propiedades.
# Esto permite reutilizar el código y crear jerarquias de clases que comparten comportamiento en común.
class Animal:
    def __init__(self, specie):
        self.specie = specie
    
    def makeSound(self):
        return 'Este animal hace un sonido'

class Dog(Animal):
    def __init__(self, specie, race):
        super().__init__(specie)
        self.race = race

    def bark(self):
        return 'El perro está ladrando'

# El método __init__() llama al método __init__() de Animal utilizando la funcion super().__init__() para inicializar la propiedad especie. Además, Perro añade una propiedad raza y un método bark()

myDog = Dog('Canino', 'Labrador')
print(myDog.specie) # => 'Canino'
print(myDog.race) # => 'Labrador'
print(myDog.makeSound()) # => 'Este animal hace un sonido'
print(myDog.bark()) # => 'El perro está ladrando'

# La herencia permite desarrollar un código más modular y escalable