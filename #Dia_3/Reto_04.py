# En este desafío, debes dibujar un triángulo equilatero usando bucles.

# Recibirás dos parámetros: size y character, que definen el número de 
# filas que tendrá y el carácter con el que se debe construir el 
# triángulo, respectivamente. Además, el triángulo debe estar 
# alineado al centro, lo que significa que la misma cantidad 
# de caracteres debe haber en ambos lados.

# Recuerda que para hacer el salto de línea debes usar "\n", no olvides 
# removerla de la última parte, debes retornar todo esto en una variable.

# Tendrás inputs y outputs como los siguientes 👇

# Ejemplo 1:
# Input: printTriangle(3, "*")
# Output:
#   *
#  ***
# *****

# Ejemplo 2:
# Input: printTriangle(6, "$")
# Output:
#      $
#     $$$
#    $$$$$
#   $$$$$$$
#  $$$$$$$$$
# $$$$$$$$$$$

# Solución
def print_triangle(size, character):
    blank_spaces = size - 1
    pieces = 1
    triangle = ''
    for i in range(1, size + 1):
        if i != 1 and i < size:
            triangle = triangle + "\n" + " " * blank_spaces + character * pieces
        elif i == 1:
            triangle = " "*blank_spaces + character *pieces
        else:
            triangle = triangle + "\n" + character *pieces
        pieces += 2
        blank_spaces -= 1
    print(triangle)
    return triangle

print_triangle(5,"$")

