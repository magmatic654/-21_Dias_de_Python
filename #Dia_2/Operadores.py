# Operadores Aritmeticos
# Suma +
print(5 + 3) # output => 8

# Resta -
print(10 - 5) # output => 5

# Multiplicación *
print(7 - 4) # output => 3

# División /
print(35 / 5) # output => 7.0

# División Entera // (veces que cabe el número sin decimales)
print(25 // 10) # output => 2

# Modulo % (resto de la división)
print(25 % 7) # output => 4

# Potencia **
print(10 ** 3) # output => 1000

####################################################################
# Operadores de asignación (Asignan valores a variables)
x = 15

# Suma
x += 5 # x = x + 5
print(x) # output => 20

# Resta
x -= 6 # x = x - 6
print(x) # output => 14

# Multiplicación
x *= 2 # x = x * 2
print(x) # output => 28

# División
x /= 7 # x = x / 7
print(x) # output => 4.0

####################################################################
# Operadores de comparación (Devuelven True o False dependiendo si 
# la comparación se cumple o no)

# Mayor que
print(10 > 4) # output => True
print(4 > 7) # output => False
print(5 > 5) # output => False

# Menor que 
print(3 < 9) # output => True 
print(7 < 7) # output => False
print(4 < 2) # output => False

# Mayor o igual que
print(7 >= 2) # output => True
print(4 >= 4) # output => True
print(2 >= 6) # output => False

# Menor o igual que
print(120 <= 510) # output => True
print(28 <= 28) # output => True
print(42 <= 35) # output => False

# Diferente que
print(12 != 5) # output => True
print(7 != 2) # output => True
print(8 != 8) # output => False

# Igual que
print(8 == 8) # output => True
print(8 == "8") # output => False 
print(8 is "8") # output => False

# 8 no es igual a "8" porque son distintos tipos de datos, uno 
# de ellos es un number y el otro es un string, por esa razón 
# al preguntar si son iguales nos arroja False

####################################################################
# Operadores logicos en Python

# and (Devuelve verdadero si ambas condiciones se cumplen)

edad = 18
cedula = True
if edad >= 18 and cedula:
    print("Puedes pasar") # output => "Puedes pasar"
else:
    print("No puedes pasar")

edad = 18
cedula = False
if edad >= 18 and cedula:
    print("Puedes pasar")
else:
    print("No puedes pasar") # output => "No puedes pasar"

# or (Devuelve verdadero si alguna de ambas condiciones se cumple)

credito = 500
vip_pass = True
if credito >= 120 or vip_pass:
    if vip_pass:
        print("Usuario VIP") # output => "Usuario VIP"
    else:
        credito -= 120
    print("Puedes pasar") # output => "Puedes pasar"
else:
    print("No puedes pasar")

# not (Invierte el valor de la expresión)

shop_open = True
if not shop_open:
    print("Tienda cerrada")
else:
    print("Tienda abierta")
