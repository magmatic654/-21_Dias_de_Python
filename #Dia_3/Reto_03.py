# En este desafío de Python, debes crear la lógica de la función 
# is_leap_year, que determina si un año es bisiesto o no. 

# Un año es bisiesto si cumple con las siguientes condiciones:
# Es divisible por 4, pero no por 100.
# Si es divisible por 100 debe serlo por 400 también.
# La función is_leap_year recibe un único parámetro: el año a evaluar. 
# Debe devolver True si el año es bisiesto o False en caso contrario.

# Toma en cuenta que la función debe ser capaz de manejar valores 
# no enteros o negativos.

# Ejemplo 1:
# Input: 2000;
# Output: true;

# Ejemplo 2:
# Input: -2024;
# Output: false;

# Ejemplo 3:
# Input: 1984.25;
# Output: false;

def is_leap_year(year):
    if year > 0:
        if year % 4 == 0 and year % 100 != 0:
            return True
        if year % 100 == 0 and year % 400 == 0:
            return True
    return False
    
    
year_1 = is_leap_year(-4)
print(year_1)