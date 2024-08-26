#  estructuras de control
# if - el bloque de código contenido en if solo se ejecutará si y solo 
# si la propocicion evaluada es verdadera
edad = 18
edad_minima = 18
if edad >= edad_minima:
    print("Puedes pasar")

# else - es el bloque de codigo que se ejecuta si la proposición de if 
# no es verdadera
edad = 18
edad_minima = 18
if edad >= edad_minima:
    print("Puedes pasar")
else:
    print("No puedes pasar, tu edad es:", 
          edad, "años y la edad minima es:", 
          edad_minima, "años")
    
# elif permite utilizar varios if en una misma estructura, 
# cuando uno de ellos es verdadero, se ejecutará ese bloque de
# código y aunque hayan más elif se saltará hasta el final de la 
# estructura de if - elif - else

calificacion: int = 100

if calificacion >= 95:
    print("Calificación Sobresaliente: A+")
elif calificacion >= 90:
    print("Calificación Extraordinaria: A")
elif calificacion >= 80:
    print("Calificación Buena: B")
elif calificacion >= 70:
    print("Calificación Regular: C")
else:
    print("Calificación Insuficiente")