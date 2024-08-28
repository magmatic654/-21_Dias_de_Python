# En este desafío, te encuentras trabajando para una empresa de transporte 
# de carga que necesita llevar un registro de los paquetes que se envían 
# en cada viaje.
# Para ello, se te proporcionará una lista de tuplas, cada una de las cuales
# representará un paquete y tendrá las siguientes propiedades:

# (id, weight, destination)

# A partir de esta información, debes crear una función 
# que calcule el peso total de los paquetes, 
# así como la cantidad de paquetes que se enviarán a cada destino. 
# Para ello, debes retornar un nuevo diccionario 
# que tenga las siguientes propiedades:

# "total_weight": El peso total de los paquetes.
# "destinations": Un diccionario con los destinos como claves y la cantidad de paquetes como valores.
# Es importante mencionar que la función debe redondear el peso total a dos decimales y que cada destino debe aparecer sólo una vez en el diccionario.

# Ejemplo:
# Input:

# [
#   (1, 20, "Mexico"),
#   (2, 15.5, "Colombia"),
#   (3, 30, "Mexico"),
#   (4, 12, "Argentina"),
#   (5, 8.2, "Colombia"),
#   (6, 25, "Mexico"),
#   (7, 18.7, "Argentina"),
#   (8, 5, "Colombia"),
#   (9, 22.3, "Argentina"),
#   (10, 14.8, "Colombia")
# ]

# Output:

# {
#   "total_weight": 171.50,
#   "destinations": {
#     "Mexico": 3,
#     "Colombia": 4,
#     "Argentina": 3
#   }
# }

packages_1 = [
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
]

def get_packages_info(packages):
    new_packages = {
        'total_weight': float(),
        'destinations': dict() 
    }
    countries = new_packages["destinations"]

    total_weight = float()
    for package in packages:
        total_weight += package[1]

        if not package[2] in countries:
            countries.update({package[2]: 1})
        else:
            if package[2] in countries:
                countries[package[2]] += 1
    
    new_packages["total_weight"] = round(total_weight, 2)
    
    return new_packages
        
        

get_packages_info(packages_1)

