# El manejo de errores y excepciones es una forma de garantizar que aunque haya una situacion inesperada, se pueda manejar de alguna manera.

# Loalgunos ejemplos comunes de exepciones son TypeError, NameError, ValueError, entre otros

# Bloques try - except 
# se utiliza cuando tenemos un codigo que podria causar un error en la ejecucion y funciona ejecutando el codigo, y si en algun momento presenta un error en la parte de try, entonces lo manejará con el codigo que está en except
# try:
    #codigo sospechoso
# except Exeption type:
    # Manejar la excepcion


# El bloque except puede manejar excepciones específicas o genéricas. 
# Por ejemplo:
# try:
#     # Código sospechoso
# except ValueError:
#     # Manejar la excepción ValueError
# except:
#     # Manejar cualquier otra excepción


# El bloque finally es uno que se ejecuta siempre sin importar si hay o no excepciones
# try:
#     # Código sospechoso
# except ExceptionType:
#     # Manejar la excepción
# finally:
#     # Código que se ejecuta siempre

# Cláusula raise
# La cláusula raise se utiliza para generar manualmente una excepción en Python. Esto nos permite lanzar una excepción específica cuando ocurre una condición no deseada.
# if condition:
#     raise ExceptionType("Mensaje de error")


# Por ejemplo, para generar una excepción TypeError, se puede utilizar la siguiente línea de código:

# raise TypeError("Se esperaba un tipo de dato diferente")


# Bloques try-except-else: También se puede utilizar un bloque else junto con try-except para especificar un código que se ejecutará si no se produce ninguna excepción.
# try:
#     # Código sospechoso
# except ExceptionType:
#     # Manejar la excepción
# else:
#     # Código que se ejecuta si no hay excepciones

# Bloques try-except-else: También se puede utilizar un bloque else junto con try-except para especificar un código que se ejecutará si no se produce ninguna excepción.
# try:
#     # Código sospechoso
# except ValueError as ve:
#     # Manejar excepción ValueError
# except TypeError as te:
#     # Manejar excepción TypeError