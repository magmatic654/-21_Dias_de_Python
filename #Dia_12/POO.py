# POO - Programacion Orientada a Objetos

# Clases y Objetos: 

# Una clase es una plantilla que define propiedades y comportamientos de un objeto.
# Un objeto es una instancia de una clase, es decir, que es creada a partir de una clase con sus propias caracteristicas y comportamientos.
class My_class:
    # Definicion de propiedades y metodos de la clase
    pass

# Creamos un objeto a partir de una clase de la siguiente manera:
my_object =  My_class()

# Atributos 
# Los atributos de una clase son variables que se asocian a los objetos y almacenan información especifica de cada instancia de la clase.
# Los atributos se definen dentro de la clase y se acceden utilizando la sintaxis object.attribute
class My_class:
    class_variable = 'Compartida por todos los objetos'

    def __init__(self):
        self.instance_variable = 'Propia de cada objeto' 

object = My_class()
print(object.class_variable) # => 'Compartida por todos los objetos'
print(object.instance_variable) # => 'Propia de cada objeto'

# Métodos
# Son funciones definidas dentro de una clase y se utilizan para hacer operaciones relacionadas con los objetos de la clase.
# Los métodos pueden acceder y modificar los atributos de un objeto.
# Se debe utilizar self como primer parametro para referenciarse a si mismo y acceder a los atributos y otros metodos de la clase
class My_class:
    def my_metod(self):
        print('Hola desde el metodo')
    
object = My_class()
object.my_metod() # => 'Hola desde el metodo'

# Constructor
# Es un metodo especial que se ejecuta automaticamente al crear un objeto a partir de una clase, se define utilizando el metodo __init__() y se utiliza para inicializar los atributos de la clase. 
class My_class:
    def __init__ (self, parameter):
        self.attribute = parameter

object = My_class('Valor del parametro')
print(object.attribute) # => 'Valor del parametro'

# Herencia
# La herencia permite crear clases basadas en clases existentes, la clase original se conoce como clase base o superclase y la nueva se llama clase derivada o subclase.
# La subclase hereda los atributos y métodos de la superclase, ademas de que se pueden agregar nuevos atributos o metodos, incluso modificar los ya existentes.
# Para crear una subclase se utiliza class y entre parentesis el nombre de la superclase
class SuperClass:
    # Definicion de la clase base
    pass

class SubClass(SuperClass):
    # Definicion de la subclase
    pass

# Polomorfismo
# El polimorfirmo es la capacidad de que objetos de cases distintas respondan de forma distina a un mismo mensaje
# Se logra utilizando metodos con el mismo nombre en las distintas clases.

class Animal:
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        print('Guau!')

class Cat(Animal):
    def sound(self):
        print('Miau!')

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog) # => 'Guau!'
make_sound(cat) # => 'Miau!'