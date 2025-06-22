#Definir una función que recibe como parámetros una lista de palabras y una palabra, la función deberá
#retornar si la palabra se encuentra en la lista o no.
#Definir una función que recibe como parámetros una lista de palabras y una palabra, la función deberá
#retornar la posición de la palabra si la encuentra en la lista o -1 sino la encuentra. 

def funcion(palabras, palabra):
     for i in palabras:
          if i == palabra:
               return True
     return False 
     
def funcion2(palabras, palabra):
     for i in range(len(palabras)): 
        if palabras[i] == palabra:
            return i

palabras = ["Tito", "Calderon", "333", "OP PO"]
palabra = input("Ingrese una palabra: ")

print(funcion(palabras, palabra))
print("Su palabra esta en la posicion: ", funcion2(palabras, palabra))