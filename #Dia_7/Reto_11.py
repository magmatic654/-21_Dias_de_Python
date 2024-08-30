# En este desafío, debes crear la lógica de la función find_words_with_two_vowels que encuentre las palabras que contienen
# exactamente dos vocales en una lista de palabras. Las vocales pueden ser tanto mayúsculas como minúsculas.

# Recibirás un único parámetro: una lista de palabras. La función debe devolver una nueva lista que contenga todas las palabras de la lista
# original que cumplan con la condición mencionada anteriormente. En caso de no haber palabras que cumplan con esta condición deberás retornar una lista vacía.

# Ejemplo 1:

# Input: find_words_with_two_vowels([
#   "hello",
#   "Python",
#   "world",
#   "platzi"
# ])

# Output: ["hello", "platzi"]

# Ejemplo 2:

# Input: find_words_with_two_vowels(["text", "test", "python", "example"])
# Output: []

##################################################################################################################
# Versión normal
def find_words_with_two_vowels(words):
    vowels = 'aeiouAEIOU'
    new_list = list()
    for word in words:
        vowels_count = 0
        for letter in word:
            if letter in vowels:
                vowels_count += 1
        if vowels_count == 2:
            new_list.append(word)
    return new_list

print(find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
]))
print(find_words_with_two_vowels(["text", "test", "python", "example"]))

##################################################################################################################
# Versión list comprehension con len
def find_words_with_two_vowels(words):
    new_list = [word for word in words if len([letter for letter in word if letter in 'aeiouAEIOU']) == 2]
    return new_list

print(find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
]))
print(find_words_with_two_vowels(["text", "test", "python", "example"]))

##################################################################################################################
# Versión list comprehension con sum
def find_words_with_two_vowels(words):
    new_list = [word for word in words if sum([1 for letter in word if letter in 'aeiouAEIOU']) == 2]
    return new_list

print(find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
]))
print(find_words_with_two_vowels(["text", "test", "python", "example"]))