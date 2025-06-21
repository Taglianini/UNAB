#Trabajo Final C8 - Fase Inicial - Tomas Tagliani
# Voy a hacer un sistema para administrar un comercio de gagdets y accesorios de computación.
#Area de funciones
def mostrarProd(Productos):    #Funcion simple para mostrar todos los productos sin filtros
     marca = input("Ingrese la marca que desea ver (Logitech/AMD/Acer/LG/Corsair): ")
     for producto in Productos:
        if producto[3] == marca:
            print("Producto disponible de", marca, ":", producto)
        else:
         print("Marca no disponible o sin productos.") 

     #print("Productos disponibles de", marca ," :")
     #for i in Productos:
          #print(i)
#def habdoble(Hotel):
     #print("Habitaciones dobles libres:")
     #for i in Hotel:
        #if i[3] == "doble" and i[4] == "libre":
            #print("Habitación:", i[0], i[1], "estado:", i[4])


#Programa principal
menu="""
1. Mostrar productos disponibles de una marca
2. Agregar un producto
3. Cambiar el estado de stock de un producto 
4. Actualizar precio de un producto
5. Listar por precio y categoria de un producto. #El usuario debera ingresar el tipo de Producto (Perifericos/Componente/Monitor, etc.)
6. Listar productos de una sucursal. El usuario debera ingresar la sucursal (CABA/Temperley/Adrogue)
7. Actualizar el stock de un producto
8. Mostrar productos por precio descendente
9. Eliminar un producto 
10. Salir
"""

Productos = [
     [1, "Mouse Inalambrico", "Perifericos","Logitech","Logitech g309","Oferta", 1500, 30,"CABA"],
     [2, "Teclado Mecánico", "Perifericos","Logitech","Logitech g413","Lista", 3000, 28,"CABA"],
     [3, "Monitor 24 pulgadas", "Monitores","LG","LG 24MP88HV-S","Lista", 12000, 20,"Adrogue"],
     [4, "Laptop Gamer", "Computadoras","Acer","Acer Predator Helios 300","Lista", 80000, 9,"Adrogue"],
     [5, "Auriculares Inalambricos", "Perifericos","Acer","Acer WH-1000XM4","Lista", 4000, 23,"CABA"],
     [6, "Disco Solido 480GB", "Componentes","Corsair","Corsair 480GB","Oferta", 7000, 50,"CABA"],
     [7, "Tarjeta Gráfica", "Componentes","AMD","RX 6500 XT 8GB","Oferta", 35000, 12,"Temperley"],
     [8, "Fuente de Poder", "Componentes","Corsair","Corsair RM750x","Lista", 10000, 25,"Temperley"],
     [9, "Procesador", "Componentes","AMD","Ryzen 7 5700F","Lista", 15000, 10,"Adrogue"],
     [10, "PC Gamer Armada", "Computadoras","AMD","Ryzen 5 3600G 16GB","Oferta", 50000, 5,"CABA"],
     [11, "Cable HDMI", "Accesorios","LG","LG Cable HDMI","Oferta", 500, 100,"CABA"],
     [12, "Mouse Pad", "Accesorios","Logitech","Logitech G440","Oferta", 1600, 80,"Adrogue"],
     [13, "Soporte para Monitor", "Monitores","LG","LG Soporte para Monitor","Lista", 2000, 40,"CABA"],
     [14, "Webcam HD", "Perifericos","Logitech","Logitech C920","Lista", 4300, 30,"Temperley"],
     [15, "Microfono USB", "Perifericos","Corsair","Corsair Void Elite","Lista", 1800, 35,"Temperley"],
     [16, "Soporte Auriculares", "Accesorios","Corsair","Corsair Soporte para Auriculares","Oferta", 900, 60,"CABA"],
     [17, "Teclado de Membrana", "Perifericos","Logitech","Logitech K120","Oferta", 1000, 70,"CABA"],
     [18, "Joystick", "Perifericos","Logitech","Logitech F310","Lista", 2000, 55,"Adrogue"],
     [19, "Cable de Red", "Accesorios","Acer","Acer Cable de Red","Lista", 300, 120,"Adrogue"],
     [20, "Memoria RAM 16GB", "Componentes","Corsair","Corsair Vengeance LPX 16GB","Oferta", 5000, 30,"Temperley"]
]

print("Bienvenido a Hardware Tagliani Store!")

print(menu)

opcion = int(input("Ingrese una opción del menú: "))

while opcion != 10:
    if opcion == 1:
        mostrarProd(Productos)
    #elif opcion == 2:
        #edit(Hotel)
    #elif opcion == 3:
        #agr(Hotel)
        #print("Cambiado con exto")
    #elif opcion == 4:
        #actprecio(Hotel)
    #elif opcion == 5:
        #subirprecio(Hotel)
    else:
        print("Opción no válida")
    print(menu)
    opcion = int(input("Ingrese una opción: "))

print("Gracias por su visita")