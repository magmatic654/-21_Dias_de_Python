# La abstraccion permite representar objetos y sus caracteristicas de manera simplificada, ocultando los detalles internos de su implementación.

# Clases y Objetos
class MyClass:
    # Definicion de propiedades y métodos de la clase
    pass

# Crear un objeto
object = MyClass()

# Métodos
# Los metodos son funciones definidas dentro de una clase y representan el comportamiento de un objeto.
# Los métodos pueden interactuar con los objetos y realizar operaciones especificas, pueden recibir parametros y acceder a las propiedades del objeto a traves del parametro self.
# Los métodos son la forma más sencilla para interactuar con el objeto sin conocer los detalles internos.
class Myclass():
    def method(self, parameter):
        # Código del método
        pass

# Herencia.
# La herencia permite crear nuevas clases basadas en clases ya existentes, se les llama subclase o clase derivada a aquellas que salieron de una superclase o clase base. Las clases derivadas o subclases heredan los métodos y propiedades de la superclase. para definir una subclase ponemos class y seguido entre parentesis la superclase.
class SuperClass:
    # Definicion de la clase base
    pass

class SubClass(SuperClass):
    # Definicion de la subclase
    pass

# La subclase puede añadir nuevos metodos o atributos de la superclase o tambien puede modificarlos.
class SuperClass:
    def superClass_Method(self):
        # Codigo del método base
        pass

class SubClass(SuperClass):
    def subClass_Method(self):
        # Codigo del método de la subclase
        pass

# Sobreescritura de Métodos
# Permite redefinir un método heredado de la superclase.
class SuperClass:
    def method(self):
        # Código del método base
        pass

class SubClass(SuperClass):
    def method(self):
        # Código del metodo modificado
        pass
