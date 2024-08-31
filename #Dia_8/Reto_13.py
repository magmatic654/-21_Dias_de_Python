# En este desafío implementarás una función que filtre los mensajes de un usuario específico. 

# La función filter_user_messages recibirá dos parámetros:
# messages: una lista de mensajes
# user: un nombre de usuario.

# Debe devolver una nueva lista que contenga solo los mensajes del usuario especificado.

# La lista messages contiene diccionarios con información sobre cada mensaje, incluyendo el remitente ('sender') y el contenido del mensaje ('content').

# En caso de no encontrar mensajes del usuario deberá retornar una lista vacía []

# Ejemplo 1:

# Input:

# messages = [
#   {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
#   {'sender': 'Bob', 'content': '¡Bien, gracias!'},
#   {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
#   {'sender': 'Charlie', 'content': 'Hola a todos.'},
#   {'sender': 'Alice', 'content': 'Nos vemos luego.'}
# ]

# user = 'Alice'
# filter_user_messages(messages, user)

# Output:

# [
#   {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
#   {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
#   {'sender': 'Alice', 'content': 'Nos vemos luego.'}
# ]

messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]
user = 'Bob'

# Utilizando funciones anonimas lambda
filter_user_messages = lambda messages, user: list(filter(lambda messages: user == messages['sender'], messages ))
print(filter_user_messages(messages, user))

# Utilizando funciones normales con list comprehension
def filter_user_messages_n(messages, user):
    return [message for message in messages if message['sender'] == user]

print(filter_user_messages_n(messages, user))

# Utilizando funciones anonimas con list comprehension
filter_user_messages_c = lambda messages, user: [message for message in messages if message['sender'] == user]

print(filter_user_messages_c(messages, user))

import timeit

timer_a = timeit.Timer(lambda: filter_user_messages(messages, user))
timer_b = timeit.Timer(lambda: filter_user_messages_n(messages, user))
timer_c = timeit.Timer(lambda: filter_user_messages_c(messages, user))

num_runs = 10000

# Mide los tiempos de ejecución
time_a = timer_a.timeit(number=num_runs)
time_b = timer_b.timeit(number=num_runs)
time_c = timer_c.timeit(number=num_runs)

print(f"Tiempo de ejecución de función_a: {time_a:.6f} segundos")
print(f"Tiempo de ejecución de función_b: {time_b:.6f} segundos")
print(f"Tiempo de ejecución de función_c: {time_c:.6f} segundos")

