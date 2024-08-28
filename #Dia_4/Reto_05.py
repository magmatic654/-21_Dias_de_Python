# En este desafío, debes encontrar al gatito más famoso con base en su 
# número de seguidores.

# Recibirás una lista de diccionarios que incluirán las siguientes 
# propiedades:

# "name": nombre del gatito.
# "followers": una lista de números, donde cada uno representa los 
# seguidores de cada red social.

# Tu tarea es devolver una lista con los nombres de los gatos que tienen 
# solo el mayor número de seguidores. 
# 
# Si hay dos o más gatos con el mismo número máximo de seguidores, 
# deberás incluirlos en la lista resultante, manteniendo el orden en 
# el que aparecen en la lista de entrada.

# Tendrás inputs y outputs como los siguientes 👇

# Ejemplo 1:
# Input: find_famous_cat([
#   {
#     "name": "Luna",
#     "followers": [500, 200, 300]
#   },
#   {
#     "name": "Michi",
#     "followers": [100, 300]
#   },
# ])

# Output: ["Luna"]

# Ejemplo 2:
# Input: find_famous_cat([
#   {
#     "name": "Mimi",
#     "followers": [320, 120, 70]
#   },
#   {
#     "name": "Milo",
#     "followers": [400, 300, 100, 200]
#   },
#   {
#     "name": "Gizmo",
#     "followers": [250, 750]
#   }
# ])

# Output: ["Milo", "Gizmo"]


cats_list_1 = [
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  },
  {
    "name": "Yusepe",
    "followers": [250, 750]
  },
  {
    "name": "Gary",
    "followers": [500, 200, 200, 100, 1]
  }
]

# Propuesta #1
##########################################################
import copy

def find_famous_cat(cats_list):
    
    famous_cat = []
    cats_list_copy = copy.deepcopy(cats_list)
    # funcion para añadir el atributo de total de seguidores a cada gato de la lista 
    append_total_followers(cats_list_copy) 

    def myFunc(cat):
        return cat['total_followers'] 
    # Ordena la lista de mayor a menor en funcion de los followers
    cats_list_copy.sort(key=myFunc, reverse=True) 

    max_followers = cats_list_copy[0]['total_followers']
    for i in range(len(cats_list_copy)):
        cat = cats_list_copy[i]
        cat_total_followers = cat['total_followers']
        if cat_total_followers == max_followers:
            famous_cat.append(cat['name'])
    return famous_cat

# Agrega a la lista un nuevo atributo para cada gato
# que contiene el numero total de seguidores de ese gato
def append_total_followers(cats_list):
    
    size_cat_list = len(cats_list) 
    for i in range(size_cat_list): 
        size_followers_list = cats_list[i]['followers'] 
        cat = cats_list[i] 
        cat_followers = cat['followers']
        total_followers = 0 
         # ciclo en base al tamaño de la lista de seguidores para sumar los seguidores al total
        for j in range(len(size_followers_list)):
            followers = cat_followers[j] 
            total_followers += followers 
        # agrega el total de seguidores en el gato correpondiente
        cat['total_followers'] = total_followers 

print("Propuesta #1:",find_famous_cat(cats_list_1))

# Propuesta #2
########################################################################

def find_famous_cat(cats_list):
    max_followers = 0
    famous_cat = []

    # Encuentra el numero maximo de seguidores
    for i in range(len(cats_list)):
        cat = cats_list[i]
        cat_followers_list = cat['followers']
        cat_followers = 0
        
        for followers in cat_followers_list:
            cat_followers += followers
        if cat_followers >= max_followers:
            max_followers = cat_followers

    # agrega a los gatos que tengan el número maximo de seguidores a la lista de famous_cat
    for i in range(len(cats_list)):
        cat = cats_list[i]
        cat_followers_list = cat['followers']
        cat_followers = 0
        for followers in cat_followers_list:
            cat_followers += followers
        
        if cat_followers == max_followers:
            famous_cat.append(cat['name'])

    return famous_cat

print("Propuesta #2:",find_famous_cat(cats_list_1))

# Propuesta #3
########################################################################

def find_famous_cat(cats_list):
    max_followers = 0
    famous_cat = []

    for i in cats_list:
        cat_followers = 0
        for j in i['followers']:
            cat_followers += j
        if len(famous_cat) == 0:
            famous_cat.append(i['name'])
            max_followers = cat_followers
        elif cat_followers > max_followers:
            max_followers = cat_followers
            del famous_cat[:]
            famous_cat.append(i['name'])
        elif cat_followers == max_followers:
            famous_cat.append(i['name'])
        else:
            continue
    return famous_cat
            

print("Propuesta #3:",find_famous_cat(cats_list_1))