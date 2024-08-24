# En este desafío encontrarás una función llamada solution que recibe 
# un parámetro llamado valor. Debes encontrar el tipo de dato del 
# parámetro valor y retornarlo desde la función solution.

# Recuerda que el parámetro valor será distinto por cada distinta forma 
# en que ejecutemos la función solution.

# Ejemplo 1:

# Input:
# solution(1)
# solution("Dieguillo")
# solution(True)

# Output:
# "number"
# "string"
# "boolean"

# Solución
def found_type(value):
   # Tu código aquí 👇
   return type(value)

print(found_type("Hola"))
print(found_type(5))
print(found_type(True))