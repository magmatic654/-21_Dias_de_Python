# Los ciclos sirven para repetir un bloque de codigo
# repetidas veces en funcion de una condición
# especifica

# for 
# se utiliza para repetir un bloque de código 
# un número especifico de veces

# for varieble in secuencia:
    # codigo a ejecutar

# se imprimiran los números del 1 al 10
for i in range(1,11):
    print(i) 

# for in se utiliza también para recorrer los
# elementos de una lista o diccionarios

# Diccionario
automovil = {
    "Marca": "Chevrolet",
    "Año": 2019,
    "Matricula": "F0VX-Z303"
}

for clave in automovil:
    print(clave) # retorna las clave de nuestro diccionario 
    print(automovil[clave]) # retorna los valores de nuestras claves en el diccionario

# Outputs:
# Marca - Clave
# Chevrolet - Valor
# Año - Clave
# 2019 - Valor
# Matricula - Clave
# F0VX-Z303 - Valor

# Lista
technologies = ["Python", "Java", "AWS"]

for element in technologies:
    print(element)

#################################################################################
# ciclo while se utiliza para cuando no sabemos cuando 
# va a terminar el programa y damos una condición logica
# hasta que deje de cumplirse el ciclo dejará de ejecutarse

i = 1
while i <= 10:
    print(i)
    i += 1

# ciclo do while simulado
# podemos hacer un do while simulado si le damos a un while como
# condicion un True, con esto se ejecutará al menos una vez y 
# ponemos dentro del ciclo una condición de salida si es que se cumple

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break # rompe el ciclo y sale del while
