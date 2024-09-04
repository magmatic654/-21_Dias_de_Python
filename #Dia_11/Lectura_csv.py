# Abrir un archivo en python

# r - read
# r+ - read and write
# w - write (crea el archivo si no existe)
# w+ - read, write and overwrite (crea el archivo si no existe)
#file = open('archivo.txt', r)

# Podemos leer todo el contenido del archivo de texto con .read()
# content = file.read()
# print(content)

# Podemos leer linea por linea el archivo de texto con .readline()
# line = file.readline()
# while line:
#   print(line)
#   line = file.readline()

# podemos leer todas las lineas y almacenarlas con .readlines()
# lines = file.readlines()
# for line in lines:
#   print(line)

# Debemos cerrar el archivo una vez hayamos dejado de utilizarlo close()
# file.close()

# es importante la apertura y cierre del archivo para asegurar una manipulacion adecuada y evitar problemas de acceso o perdida de datos
# try:
#   file = open('text.txt', 'r')
#   # Realizar operaciones con lectura
# finally:
#   file.close()

# o utilizando el bloque with:
# with open('archivo.txt', 'r') as file:
#   Realizar operaciones de lectura


# Leer csv (Comma-Separated Values)
####################################################################
# debemos importar el modulo csv para obtener las funciones y clases necesarias
# import csv

# Abrir un archivo csv con .open() y especificando el modo 'r', 'w', etc.
# with open('archivo.csv', 'r') as file
    # Realizar operaciones de lectura del archivo csv

# Es necesario crear un objeto de lectura para poder leer csv utilizando reader() del modulo csv que permite acceder a los datos fila por fila
# with open('archivo.csv', 'r') as file
    # csv_reader = csv.reader(file)
    # Realizar operaciones de lectura del archivo csv

# Pordemos leer cada fila del archivo csv utilizando un for
# with open('archivo.csv', 'r') as file
#   csv_reader = csv.reader(file)
#   for row in csv_reader:
#       # Acceder a los valores de cada columna en la fila
#       # print(row) 

# Leer datos en diccionarios: Si el archivo csv tiene una fila en el encabezado que contiene los nombres de las columnas, podemos leer los datos en forma de diccionarios utilizando el objeto lector csv con el metodo DictReader().
# with open('archivo.csv', 'r') as file
#   csv_reader = csv.reader(file)
#   for row in csv_reader:
#       # Acceder a los valores utilizando los nombres de las columnas
#       # print(row['columna1'], row['columna2']) 


# Es importante tener en cuenta que los archivos CSV pueden tener diferentes delimitadores, como comas, punto y coma o tabulaciones. Si el archivo CSV utiliza un delimitador distinto de la coma, podemos especificarlo al crear el objeto lector CSV utilizando el parámetro delimiter.