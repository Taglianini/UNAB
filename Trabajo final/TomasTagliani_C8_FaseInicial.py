#Trabajo Final C8 - Fase Inicial - Tomas Tagliani
# Voy a hacer un sistema para administrar un comercio de gagdets y accesorios de computación.
#Area de funciones
def mostrarProd(Productos):    #Funcion simple para mostrar todos los productos sin filtros
     print("Productos disponibles: ")
     for i in Productos:
          print(i)


#Programa principal
menu="""
1. Mostrar productos disponibles 
2. Agregar un producto
3. Cambiar el estado de stock de un producto
4. Actualizar precio de un producto
5. Actualizar el precio de todos los productos en un 10% 
6. Mostrar productos de una categoria 
7. Mostrar productos por precio ascendente
8. Mostrar productos por precio descendente
9. Eliminar un producto 
10. Salir
"""

Productos = [
     [1, "Mouse Inalambrico", "Perifericos", 1500, 30],
     [2, "Teclado Mecánico", "Perifericos", 3000, 28],
     [3, "Monitor 24 pulgadas", "Monitores", 12000, 20],
     [4, "Laptop Gamer", "Computadoras", 80000, 9],
     [5, "Auriculares Inalambricos", "Perifericos", 4000, 23],
     [6, "Disco Solido 480GB", "Componentes", 7000, 50],
     [7, "Tarjeta Gráfica", "Componentes", 35000, 12],
     [8, "Fuente de Poder", "Componentes", 10000, 25],
     [9, "Procesador Intel", "Componentes", 15000, 10],
     [10, "PC Armada Intel con Tarjeta Grafica", "Computadoras", 50000, 5],
     [11, "Cable HDMI", "Accesorios", 500, 100],
     [12, "Mouse Pad Logitech", "Accesorios", 1600, 80],
     [13, "Soporte para Monitor", "Monitores", 2000, 40],
     [14, "Webcam HD", "Perifericos", 4300, 30],
     [15, "Microfono USB", "Perifericos", 1800, 35],
     [16, "Soporte Auriculares", "Accesorios", 900, 60],
     [17, "Teclado de Membrana", "Perifericos", 1000, 70],
     [18, "Joystick", "Perifericos", 2000, 55],
     [19, "Cable de Red", "Accesorios", 300, 120],
     [20, "Memoria RAM 16GB", "Componentes", 5000, 30]
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