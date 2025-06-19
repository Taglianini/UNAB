#Area de funciones
def agrega_pas(lista):
     apellido = input("ingresa tu apellido: ")
     edad = int(input("ingresa tu edad: ")) 
     ciudad = input("ingresa tu ciudad de destino: ")
     nuevo_pasajero = [apellido, edad, ciudad]
     lista.append(nuevo_pasajero)
     return lista
#Programa Principal
pasajeros = [["Torres", 25, "Mendoza"],["Perez", 15, "Salta"],["Saavedra", 20, "Bahia Blanca"]]
pasajeros_act = agrega_pas(pasajeros)
print("Lista de pasajeros:", pasajeros_act)