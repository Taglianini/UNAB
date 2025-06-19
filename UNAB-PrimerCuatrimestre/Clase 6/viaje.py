#Nos contratan para realizar un sistema para Administrar una Agencia de Transportes
#“Destinos Florencio” se tiene la siguiente información: número de viaje, patente,
#ciudad de origen, ciudad destino, fecha (dd/mm/aaaa) , cantidad de pasajes
#vendidos, precio, estado (Programado/ En viaje/cancelado)
#Realice una función que realice la carga de datos, se finaliza la carga cuando se
#ingresa como Numero de viaje 0.\
#Area de Funciones
def cargadatos():
     viajes=[]
     numviaje=int(input("Ingrese el numero de viaje: "))
     while (numviaje!=0):
          patente=input("Ingrese la patente: ")
          ciudad_origen = input("Ciudad de origen: ")
          ciudad_destino = input("Ciudad destino: ")
          fecha = input("Fecha (dd/mm/aaaa): ")
          cantidad_pasajes = int(input("Cantidad de pasajes vendidos: "))
          precio = float(input("Precio del pasaje: "))
          estado=input("Ingrese el estado (programado/en viaje/cancelado): ")
          pasajero=[numviaje, patente, ciudad_origen, ciudad_destino, fecha, cantidad_pasajes, precio, estado]
          viajes.append(pasajero)
          numviaje=int(input("Ingrese el nuevo numero de viaje: "))
     return viajes 

#Programa Principal
lista_pasajeros=cargadatos()
for i in lista_pasajeros: 
     print(i)