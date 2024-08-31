# High Order Functions son funciones que cumplen alguno de los siguientes criterios:

# - Toman una o más funciones como argumentos
# - devuelven una funcion como resultado

# High Order Functions comunes:

# map(function, sequence): Aplica la funcion a cada elemento de la secuencia y devuelve un iterador con los resultados
# Ejemplo
numbers = [1,2,3,4,5,6]
duplicade = list(map(lambda x: f'x = {x} => {x*2}', numbers))
print(duplicade)

# filter(function, sequence): filtra los elementos en secuancia según la funcion dada y devuelve un iterador con los elementos que cumplan la condicion

# Ejemplo
words = ['cancion', 'ave', 'pelo' 'dodo', 'cancion','ave', 'dodo']
def find_words(inSeach):
    return list(filter(lambda word: inSeach == word, words))
print(find_words('cancion')) # => ['cancion', 'cancion']

# reduce(function, sequence): Aplica la funcion a los elementos de la secuencia  de manera acumulatica, reduciendolos a un solo valor
# debe importarse
from functools import reduce
summation = reduce(lambda x, y: x + y, numbers)
print(summation) # => 21

# sorted(sequence, key=function): Ordena la secuencia según la funcion de clave dada y devuelve una nueva lista con los elementos ordenados

#Ejemplos
numbers_v2 = [1, 5, 7, 3, 10, 9, 6]
print(sorted(numbers_v2))  # => [1, 3, 5, 6, 7, 9, 10]

# reverse = True - Se invierte el orden
print(sorted(numbers_v2, reverse=True)) # => [10, 9, 7, 6, 5, 3, 1]

# key = len - Se ordena por numero de palabras
words_v2 = ['Llama', 'Bocina', 'Soda', 'Puerta', 'Fernando', 'Pista']
print(sorted(words_v2, key=len)) # => ['Soda', 'Llama', 'Pista', 'Bocina', 'Puerta', 'Fernando']