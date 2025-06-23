#Trabajo Final C8 - Fase Inicial - Tomas Tagliani
# Voy a hacer un sistema para administrar un comercio de gagdets y accesorios de computación.
#Area de funciones
def mostrarProd(Productos):
     marca = input("Ingrese la marca que desea ver (Logitech/AMD/Acer/LG/Corsair): ").lower()
     for producto in Productos:
        if producto[2].lower() == marca:
            print("Productos disponibles:", producto)

def agrProd(Productos):
    prod = input("Ingrese el nombre del producto: ")
    cat = input("Ingrese la categoria del producto (Perifericos/Monitores/Computadoras/Componentes/Accesorios): ")
    marca = input("Ingrese la marca del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    sucursal = input("Ingrese la sucursal en la que esta disponible (CABA/Adrogue/Temperley): ")
    prodnuevo = [prod, cat, marca, precio, stock, sucursal]
    Productos.append(prodnuevo)
    print("Producto agregado con exito")
    return Productos 

def actStock(Productos):
    for prod in Productos:
        print(prod[6])

def actPrecio(Productos):
    for i in Productos:
        print(i[5])




#Programa principal
menu="""
1. Mostrar productos disponibles de una marca
2. Agregar un producto
3. Cambiar el estado de stock de un producto 
4. Actualizar precio de todos los productos 
5. Listar por precio y categoria de un producto. #El usuario debera ingresar el tipo de Producto (Perifericos/Componente/Monitor, etc.)
6. Listar productos de una sucursal. El usuario debera ingresar la sucursal (CABA/Temperley/Adrogue)
7. Eliminar un producto 
8. Salir
"""

Productos = [
     ["Mouse Inalambrico", "Perifericos","Logitech","Logitech g309","Oferta", 1500, 30,"CABA"],
     ["Teclado Mecánico", "Perifericos","Logitech","Logitech g413","Lista", 3000, 28,"CABA"],
     ["Monitor 24 pulgadas", "Monitores","LG","LG 24MP88HV-S","Lista", 12000, 20,"Adrogue"],
     ["Laptop Gamer", "Computadoras","Acer","Acer Predator Helios 300","Lista", 80000, 9,"Adrogue"],
     ["Auriculares Inalambricos", "Perifericos","Acer","Acer WH-1000XM4","Lista", 4000, 23,"CABA"],
     ["Disco Solido 480GB", "Componentes","Corsair","Corsair 480GB","Oferta", 7000, 50,"CABA"],
     ["Tarjeta Gráfica", "Componentes","AMD","RX 6500 XT 8GB","Oferta", 35000, 12,"Temperley"],
     ["Fuente de Poder", "Componentes","Corsair","Corsair RM750x","Lista", 10000, 25,"Temperley"],
     ["Procesador", "Componentes","AMD","Ryzen 7 5700F","Lista", 15000, 10,"Adrogue"],
     ["PC Gamer Armada", "Computadoras","AMD","Ryzen 5 3600G 16GB","Oferta", 50000, 5,"CABA"],
     ["Cable HDMI", "Accesorios","LG","LG Cable HDMI","Oferta", 500, 100,"CABA"],
     ["Mouse Pad", "Accesorios","Logitech","Logitech G440","Oferta", 1600, 80,"Adrogue"],
     ["Soporte para Monitor", "Monitores","LG","LG Soporte para Monitor","Lista", 2000, 40,"CABA"],
     ["Webcam HD", "Perifericos","Logitech","Logitech C920","Lista", 4300, 30,"Temperley"],
     ["Microfono USB", "Perifericos","Corsair","Corsair Void Elite","Lista", 1800, 35,"Temperley"],
     ["Soporte Auriculares", "Accesorios","Corsair","Corsair Soporte para Auriculares","Oferta", 900, 60,"CABA"],
     ["Teclado de Membrana", "Perifericos","Logitech","Logitech K120","Oferta", 1000, 70,"CABA"],
     ["Joystick", "Perifericos","Logitech","Logitech F310","Lista", 2000, 55,"Adrogue"],
     ["Cable de Red", "Accesorios","Acer","Acer Cable de Red","Lista", 300, 120,"Adrogue"],
     ["Memoria RAM 16GB", "Componentes","Corsair","Corsair Vengeance LPX 16GB","Oferta", 5000, 30,"Temperley"]
]

print("Bienvenido a Hardware Tagliani Store!")

print(menu)

opcion = int(input("Ingrese una opción del menú: "))

while opcion != 8:
    if opcion == 1:
        mostrarProd(Productos)
    elif opcion == 2:
        Productos = agrProd(Productos)
    elif opcion == 3:
        actStock(Productos)
        print("Cambiado con exito")
    #elif opcion == 4:
        #actprecio(Hotel)
    #elif opcion == 5:
        #subirprecio(Hotel)
    else:
        print("Opción no válida")
    print(menu)
    opcion = int(input("Ingrese una opción: "))

print("Gracias por su visita")