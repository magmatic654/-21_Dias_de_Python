# Encapsulamiento
# la encapsulacion se refiere a la idea de que los datos y metodos deben estar protegidos y no deben ser accedidods directamente desde fuera del objeto. En python se utilizan decoradores como @property para las propiedades.

# Convenciones y Nomenclatura
# En python se utilizan convenciones de nomenclatura para indicar el nivel de accesibilidad de los atributos y metodos de una clase.
# se utiliza(_) guión bajo al comienzo del nombre de atributo o método para inficar que es privado, es decir, que no debe ser accedido fuera de la clase.
class MyClass:
    def __init__(self):
        self._private_attribute = 10
    
    def _private_method(self):
        pass

# El decorador @property se utiliza para crear un método getter para acceder a un atributo privado como si fuera una propiedad publica.
class MyClass:
    def __init__(self):
        self._private_attribute = 10
    
    @property
    def public_attribute(self):
        return self._private_attribute
# En este ejemplo el atributo privado _private_attribute se puede acceder a el desde fuera de la clase utilizando el metodo getter public_attribute
object = MyClass()
print(object.public_attribute) # => 10

# Setter
# setter utilizando el decorador @public_attribute.setter para crear un método setter que permita modificar el atributo privado a través de una sintaxis similar a la asignacion de una propiedad.
# El método setter se denomina como la propiedad que se desea modificar y se define utilizando el decorador @public_atribute.setter
class MyClass:
    def __init__(self):
        self._private_attribute = 10
    
    @property
    def public_attribute(self):
        return self._private_attribute
    
    @public_attribute.setter
    def public_attribute(self, new_value):
        self._private_attribute = new_value
# En este ejemplo el método setter public_attribute permite modificar el atributo _private_attribute utilizando una sintaxis similar a la asignacion de una propiedad
object = MyClass()
object.public_attribute = 20
print(object.public_attribute)

# Métodos y atributos privados
# Se utiliza (_) guion bajo como convencion para los métodos y atributos privados, aunque realmente no existen restricciones de acceso se considera que los atributos y métodos que inician con doble guión bajo (__) sean tratados como privados y no sean accedidos a ellos directamente desde fuera de la clase.
# Python utiliza name mangling para cambiar el nombre de estos atributos y métodos privados por dentro de python.
class MyClass:
    def __init__(self):
        self.__private_attribute = 10
    
    def __private_method(self):
        pass
#  __private_attribute y __private_method son privados pero python los renombra internamente utilizando el nombre de la clase que los contiene para evitar conflictos con clases derivadas. 
# El atributo __private_attribute se renombraría a _MyClass__private_attribute internamente

object = MyClass()

