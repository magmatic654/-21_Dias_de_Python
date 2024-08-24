# Variables
# Las variables en python se inicializan en una sola linea de codigo, 
# además de que python asigna su tipo de variable dependiendo del valor
# asignado, pues el lenguaje determinna el tipo de variable en tiempo de
# ejecucion

# Ejemplo:
carro = "Mustang"
telefono = 5522334455

##########################################################################
# Funciones
# Las funciones se definen con la palabra def y seguido se pone el nombre
# de nuestra funcion, el que queramos, y por último se encierran entre
# parentesis los argumentos esperados y se agrega dos puntos al final
# de los parentesis def name_funcion(arg_1, arg_2, ... , arg_n):

# Ejemplo:
def suma(a, b):
    return a + b

# Para "invocar" esta funcion debemos escribir el nombre de la función
# seguido de los argumentos encerrados entre parentesis 
# name_funcion(arg_1, arg_2, ... arg_n)

# Llamada
suma(2, 4) # no visible result => 6

# Para ver el resultado de nuestra funcion podemos asignarla a una 
# variable e imprimirla

suma1 = suma(2, 4)
print(suma1) # En este caso al imprimir nuestra variable suma 1, nos da
# el resultado de la suma en pantalla. output => 6

##########################################################################
# Funciones anonimas - Lambda
# Estas funciones se declaran en usa sola linea de código
# name_funcion = lambda: paramethers

# Ejemplo:
saludar = lambda: print("Hola")
# Llamada:
saludar()

