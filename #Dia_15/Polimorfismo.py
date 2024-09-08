# Polimorfismo
# El polimorfismo permite que una interfaz pueda ser implementada por múltiples clases, permitiendo que diferentes objetos respondan de forma distinta a una misma llamada

# En python esto se logra sobreescribiendo los metodos padre dentro de las subclases.
class Animal:
    def talk(self):
        print('Sonidos de animal')

class Dog(Animal):
    def talk(self):
        print('Guau guau!')

class Cat(Animal):
    def talk(self):
        print('Miau miau!')

def talk(animal):
    animal.talk()

animal = Animal()
dog = Dog()
cat = Cat()

talk(animal)
talk(dog)
talk(cat)
# animal.talk()
# dog.talk()
# cat.talk()

# El polimorfismo permite escribir un código más modular y genérico, ya que podemos diseñar nuestras clases para que implementen una interfaz común pero con comportamientos diferentes. Reutilizando el código y flexibilizando nuestro programa