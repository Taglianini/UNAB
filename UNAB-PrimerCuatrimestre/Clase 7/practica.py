#Area de funciones
def cargadatos():
     nom=input("Ingrese el nombre: ")
     ano=int(input("Ingrese el ano de publicacion: "))
     id=input("Ingrese el idioma de la pelicula: ")
     p=input("Ingrese el pais: ")
     dir=input("Ingrese el director de la pelicula: ")
     act1=input("Ingrese el actor principal: ")
     act2=input("Ingrese un segundo actor: ")
     li=[nom, ano, id, p, dir, act1, act2]
     return li 


def fun1(peli, idioma):
     return peli[2]==idioma

def fun2(peli, director):
     return peli[4]==director  

#Programa Principal
peli1=cargadatos()
i=input("Ingrese el idioma de una pelicula: ")
d=input("Ingrese el director de la pelicula: ")
print("El resultado de saber si el idioma es el de la pelicula es: ", fun1(peli1, i),"El resultado de saber si el director es el mismo: ", fun2(peli1, d))
