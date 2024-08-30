# En este desafío, debes crear una función llamada count_words_by_length que recibe una lista de palabras y devuelve un diccionario 
# que mapea la longitud de las palabras a la cantidad de palabras que tienen esa longitud.

# Ejemplo 1:

# Input:
# count_words_by_length([
#   "apple",
#   "banana",
#   "orange",
#   "grapefruit",
#   "pear",
#   "kiwi"
# ])

# Output:
# {5: 1, 6: 2, 10: 1, 4: 2}

# Ejemplo 2:

# Input:
# count_words_by_length([
#   "apple",
#   "banana",
#   "orange"
# ])

# Output:
# {5: 1, 6: 2}

# Version normal
def count_words_by_length(words):
    new_dict = dict()
    for word in words:
        if new_dict.get(len(word)):
            new_dict[len(word)] += 1
        else:
            new_dict[len(word)] = 1
    print(new_dict)
    return new_dict


count_words_by_length([
  "apple",
  "banana",
  "orange"
])

count_words_by_length([
  "apple",
  "apple",
  "apple",
])

# Version dict comprehension
def count_words_by_length(words):
    return {len(word): sum(1 for word_ in words if len(word) == len(word_))  for word in words}



count_words_by_length([
  "apple",
  "banana",
  "orange"
])

count_words_by_length([
    "apple",
    "apple",
    "apple",
    "banana",
    "orange"
])