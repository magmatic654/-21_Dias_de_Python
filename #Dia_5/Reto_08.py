# En este desafío deberás implementar la lógica de 
# una función que cuente la cantidad de ocurrencias 
# de cada letra en una cadena de texto 
# y lo almacene en un diccionario.

# Es importante mencionar que la función debe 
# ser sensible a mayúsculas y minúsculas, es decir, 
# las letras mayúsculas y minúsculas deben considerarse diferentes.

# Ejemplo 1:
# Input: "Hola mundo"

# Output: {
#   'H': 1, 
#   'o': 2, 
#   'l': 1, 
#   'a': 1, 
#   ' ': 1, 
#   'M': 1, 
#   'u': 1, 
#   'n': 1, 
#   'd': 1
# }

# Propuesta #1
########################################################
phrase_1 = "Hola mundo"

def count_letters(phrase):
    chars_count = dict()

    for char in phrase:
        if not char in chars_count:
            chars_count.update({char: 1})
        else:
            chars_count[char] += 1
    return chars_count

r_1 = count_letters(phrase_1)
print('Propuesta 1:',r_1)

# Propuesta #2
########################################################
phrase_2 = "Hola mundo"

def count_letters(phrase):
    chars_count = dict()
    for char in phrase:
        chars_count[char] = chars_count.get(char, 0) + 1
    return chars_count

r_2 = count_letters(phrase_1)
print('Propuesta 2:',r_2)

# Propuesta #3
########################################################
phrase_3 = "Hola mundo"

def count_letters(phrase):
    chars_count = dict()
    for char in phrase:
        if not char in chars_count:
            chars_count[char] = 1
        else:
            chars_count[char] += 1
    return chars_count

r_3 = count_letters(phrase_1)
print('Propuesta 3:',r_3)
