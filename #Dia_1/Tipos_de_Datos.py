# Numbers
# Este tipo de datos representa a los numeros y pueden 
# ser enteros y números con decimales

# Ejemplos:
edad = 30
pi = 3.14
salario = 2650.50

# Notación cientifica
# Podemos utilizar notacion cientifica en python
numero_grande = 1e6 # 1 millon
numero_pequeño = 1e-6 # 0.000001

# Determinar un tipo de variable numerica para evitar errores
# Podemos tipar el dato numerico que queremos que sea 
# nuestra variable 

# Ejemplo con int:
edad: int = 30

# Ejemplo con float:
pi: float = 3.14
salario: float = 2650.50

##########################################################################
# Strings
# Este tipo de dato representa secuencias de caracteres
# Es posible crear strings en python utilizando comillas simples o dobles
# entre el texto que querramos guardar
# Ejemplos con comillas dobles:
saludo = "Hola"
nombre = "Harold"
apellido = "Rodriguez"

# Ejemplos con comillas simples:
Marca_automovil = 'Mercedes'
pais = "México"

# Los strings, igualmente que los números, pueden ser tipados 
# Ejemplo
mensaje: str = "Hola, ¿cómo estás?"

# Concatenar dos strings utilizando +
# Ejemplo
print(saludo + ", " + nombre + " " + apellido + "!") 
# output => Hola, Harold Rodriguez!

# f-strings, es otra forma de agregar strings 
# que incluyan variables y expresiones
# Ejemplo
print(f"{saludo}, {nombre} {apellido}!")
# output => Hola, Harold Rodriguez!

##########################################################################
# Métodos comunes para manipular strings
# len() Devuelve la longitud de un string
# upper() Devuelve los caracteres del string dado en mayusculas
# lower() Devuelve los caracteres del string dado en minusculas
# split() devuelve una lista de strings separadaos por un carácter

nombre = "Harold"
print(len(nombre)) # output => 6
print(nombre.upper()) # output => HAROLD
print(nombre.lower()) # output => harold
print(nombre.split('a')) # output => ['H', 'rold'] 

##########################################################################
# Diccionarios
# Permiten guardar valores con el conjunto par clave - valor, 
# estos pares son elementos del diccionario
# El diccionario se forma como si fueras a declarar una variable,
# pero despues del igual se agregan parentesis {} y dentro de ellos 
# se especifican los elementos de nuestro diccionario con la sintaxis
# clave: valor, por cada clave valor se separa con una coma al final para
# poder agregar más elementos al diccionario.
# Ejemplo:
cliente = {
    "nombre": "Robert",
    "credito": 600,
    "peliculas_rentadas": {
        "nombre": "Transformers",
        "duracion": "3 horas",
        "costo": 300
    }
}

# Acceder a los diccionarios
# Se puede acceder a los diccionarios utilizando la clave como indice.
# Ejemplo
print(cliente["nombre"]) # output => Robert
print(cliente["credito"]) # output => 600
print(cliente["peliculas_rentadas"]["nombre"]) # output => Transformers

##########################################################################
# Booleanos
# Este tipo de valor representa a un valor verdadero o falso.
# Se puede utilizar True para verdadero y False para falso
#Ejemplo
curso_terminado = True
clase_terminada = False

##########################################################################
# type
# En python podemos utilizar la función type para saber el tipo de dato 
# con el que estemos interesados
# Ejemplos:

type("#PlatziChallenge") # <class 'str'>
type(30) # <class 'int'>
type({}) # <class 'dict'>
type([]) # <class 'list'>

