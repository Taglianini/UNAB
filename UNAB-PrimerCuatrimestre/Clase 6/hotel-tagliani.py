#Nos contratan para realizar un sistema para Administrar un hotel de Hudson. Se tiene
#información del N° de habitación, tipo (simple / doble / triple/suit), estado (“ocupado”/“libre”), precio por noche.
#Realice una función que cree una lista con información del hotel. La carga de datos
#finaliza cuando se ingresa como N° de habitación 0 (cero)
#Se requiere tener un menú de opciones:
#1) Mostrar las habitaciones dobles y su precio.
#2) Informar la cantidad de habitaciones libres que hay en el hotel.
#3) Actualizar el estado de una habitación. Para ello el usuario deberá ingresar el
#N° de habitación y el nuevo estado.
#4) Informar la habitación más cara del hotel que está ocupado.
#5) Salir
#Realizar un programa que primero cargue los datos del hotel de Hudson. Luego 
#deberá mostrar el menú de opciones en forma permanente. Cada opción del menú
#se deberá desarrollar utilizando funciones.
Hotel=[[101, "1B", 1, "doble", "libre", 1000],
      [102, "2B", 1, "simple", "ocupado", 500],
      [103, "1A", 4, "triple", "libre", 1200],
      [104, "2A", 2, "suit", "libre", 1500],
      [105, "1C", 1, "doble", "libre", 1000]]

def habdoble(Hotel):
     print("Habitaciones dobles libres:")
     for i in Hotel:
        if i[3] == "doble" and i[4] == "libre":
            print("Habitación:", i[0], i[1], "estado:", i[4])

def edit(Hotel):
    num = int(input("Ingrese el número de habitación que desea cambiar: "))
    for hab in Hotel:
        if hab[0] == num:
            print("Estado actual:", hab[4])
            nuevo = input("Ingrese el nuevo estado ('libre' u 'ocupado'): ")
            if nuevo in ["libre", "ocupado"]:
                hab[4] = nuevo
                print("Estado actualizado con exito.")

def agr(Hotel):
    #101, "1B", 1, "doble", "libre", 1000
     numhab=int(input("Ingrese el nuermo de la nueva habitacin: "))
     numdep=input("Ingrese el piso y letra de la habitacion: ")
     numpis=int(input("Ingrese el piso: "))
     tipo=input("Ingrese el tipo de habitacion simple / doble / triple/suit: ")
     disp=input("ingrese su disponibilidad ocupado/libre: ")
     precio=int(input("Ingrese el precio de la habitracion:"))
     
     depnuevo=[numhab,numdep, numpis, tipo, disp, precio]
     Hotel.append(depnuevo)

def actprecio(Hotel):
    num = int(input("Ingrese el número de habitación que desea cambiar el precio: "))
    for hab in Hotel:
        if hab[0] == num:
            print("Precio actual:", hab[5])
            nuevprecio = int(input("Ingrese el nuevo precio de la habitación: "))
            hab[5] = nuevprecio
            print("Precio actualizado con exito.")
            return

def subirprecio(Hotel):
    for hab in Hotel:
        if hab[4] == "libre":
            hab[5] += hab[5] / 10 
        else:
            hab[5] += hab[5] / 20
    print("Se subieron los precios")

print("Bienvenido al Hotel Tagliani")
menu="""
1. Mostrar las habitaciones dobles libres
2. Cambiar el estado de una habitacion
3. Agregar una habitacion
4. Actualizar precio de una habitacion
5. Actualizar el precio de las habitaciones
6. Salir
"""
print(menu)

opcion = int(input("Ingrese una opción del menú: "))

while opcion != 6:
    if opcion == 1:
        habdoble(Hotel)
    elif opcion == 2:
        edit(Hotel)
    elif opcion == 3:
        agr(Hotel)
        print("Cambiado con exto")
    elif opcion == 4:
        actprecio(Hotel)
    elif opcion == 5:
        subirprecio(Hotel)
    else:
        print("Opción no válida")
    print(menu)
    opcion = int(input("Ingrese una opción: "))

print("Gracias por su visita")
     