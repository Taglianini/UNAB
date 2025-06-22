#Definir una función que recibe como parámetros una palabra y una letra y retorna todas las palabras que
#comienzan con esa letra.

def funcion(palabras, letra):
     pal = []
     for i in palabras: 
          if i[0] == letra:
               pal.append(i)
     return pal 
     

palabras = ["Gracias", "Ganador", "Rosa", "Pina colada"]
letra = input("Ingrese una letra: ")
print("Las palabras que comienza por tu letra son: ",funcion(palabras, letra))