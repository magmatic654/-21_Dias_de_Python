# En este desafío, debes crear una función que encuentre 
# el palíndromo más largo en una lista de palabras.

# Recibirás un único parámetro: una lista de palabras. 
# Si no hay ningún palíndromo en la lista, la función 
# debe devolver None. 
# 
# Si hay más de un palíndromo con la misma longitud máxima, 
# debes devolver el primer palíndromo encontrado en la lista.

# Un palíndromo es una palabra que se puede leer de la misma 
# manera tanto hacia adelante como hacia atrás.

# Ejemplo 1:

# Input: find_largest_palindrome(["racecar", "level", "world", "hello"])

# Output: "racecar"

# Ejemplo 2:

# Input: find_largest_palindrome(["Platzi", "Python", "django", "flask"])

# Output: None

# Propuesta #1
#######################################################################################
import copy
def find_largest_palindrome(words_list):
    words = list()
    palindrome = list()
    
    for word in words_list:
        letters = list()
        for char in word:
            letters.append(char)
        words.append(letters)
        words_reverese = copy.deepcopy(words)
    for word in words_reverese:
        word.reverse()

    largest = 0
    for i in range(len(words)):
        if words[i] == words_reverese[i] and len(words[i]) > largest:
            largest = len(words[i])
            del palindrome[:]
            palindrome.append(words[i])

    if len(palindrome) > 0:
        join_list = ''.join(palindrome[0])
        return join_list
    else:
        return None

# prueba_1 = find_largest_palindrome(["racecar", "level", "world", "hello"])
# print(prueba_1)
# prueba_2 = find_largest_palindrome(["Platzi", "Python", "django", "flask"])
# print(prueba_2)

# Propuesta #2
#######################################################################################
def find_largest_palindrome(words):
   largest = 0
   palindrome = ""

   for word in words:
        if word == word[::-1]:
            if len(word) > largest:
                palindrome = word
                largest = len(word)
      
   return palindrome if palindrome else None

# prueba_1 = find_largest_palindrome(["racecar", "level", "world", "hello"])
# print(prueba_1)
# prueba_2 = find_largest_palindrome(["Platzi", "Python", "django", "flask"])
# print(prueba_2)

# Propuesta #3
#######################################################################################
# Utilizando List Comprehesion
def find_largest_palindrome(words):
    palindromes = [word for word in words if word == word[::-1]]
    return max(palindromes, key=len, default=None)


prueba_1 = find_largest_palindrome(["racecar", "level", "world", "hello"])
print(prueba_1)
prueba_2 = find_largest_palindrome(["Platzi", "Python", "django", "flask"])
print(prueba_2)


# Propuesta #4
#######################################################################################
find_largest_palindrome = lambda words: max([word for word in words if word == word[::-1]], key=len, default=None)
prueba_1 = find_largest_palindrome(["racecar", "level", "world", "hello"])
print(prueba_1)
prueba_2 = find_largest_palindrome(["Platzi", "Python", "django", "flask"])
print(prueba_2)