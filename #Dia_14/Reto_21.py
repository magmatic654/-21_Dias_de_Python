# En este desafío, debes crear una jerarquía de clases mediante el uso de la herencia.

# La clase base será Animal con las propiedades name, age y specie y un método getInfo que devuelve un objeto con la información del animal.

# Luego, debes crear una clase Mammal que herede de Animal y tenga una propiedad adicional hasFur y un método getInfo que sobreescriba al del padre y incluya la información de hasFur.

# Finalmente, debes crear una clase Dog que herede de Mammal y tenga una propiedad adicional breed y un método getInfo que sobreescriba al del padre y incluya la información de breed, al igual que el método bark que devuelva el string "woof!". Las propiedades de specie y hasFur deben estar incluídas como "dog" y True respectivamente desde la implementación por lo que no debe ser necesario pasar los valores a la hora de crear la instancia.

# Ejemplo 1

# Input:
# bird = Animal("pepe", 1, "bird")
# bird.getInfo()

# Output:
# {
#   "name": "pepe",
#   "age": 1,
#   "specie": "bird",
# }

# Ejemplo 2

# Input:
# hippo = Mammal("bartolo", 3, "hippo", false)
# hippo.getInfo()

# Output:
# {
#   "name": "bartolo",
#   "age": 3,
#   "specie": "hippo",
#   "hasFur": false,
# }

# Ejemplo 3

# Input:
# dog = Dog("fido", 4, "pastor aleman");
# dog.bark()

# Output:
# "woof!"

class Animal:
    def __init__(self, name, age, specie):
        self._name = name
        self._age = age
        self._specie = specie

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def specie(self):
        return self._specie
    
    @specie.setter
    def specie(self, new_specie):
        self.specie = new_specie
    
    def getInfo(self):
        return {
            'name': self._name,
            'age': self._age,
            'specie': self._specie,
        }


class Mammal(Animal):
    def __init__(self, name, age, specie , hasFur):
        super().__init__(name, age, specie)
        self._hasFur = hasFur

    @property
    def hasFur(self):
        return self._hasFur

    @hasFur.setter
    def hasFur(self, new_hasFur):
        self._hasFur = new_hasFur
    
    def getInfo(self):
        info = super().getInfo()
        info['hasFur'] = self._hasFur
        return info
        

class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, specie = 'dog', hasFur=True)
        self._hasFur = True
        self._breed = breed
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        self._breed = new_breed
    
    def getInfo(self):
        info = super().getInfo()
        info['breed'] = self._breed
        return info

    def bark(self):
        return 'woof!'
    
bird = Animal("pepe", 1, "bird")
print(bird.getInfo())

hippo = Mammal("bartolo", 3, "hippo", False)
print(hippo.getInfo())

dog = Dog("fido", 4, "pastor aleman")
print(dog.bark())