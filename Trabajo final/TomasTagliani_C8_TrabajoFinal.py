#Trabajo Final C8 - Fase Inicial - Tomas Tagliani
# Voy a hacer un sistema para administrar un comercio de gagdets y accesorios de computación.
#TRABAJO APROBADO - PROMOCION PRIMER CUATRIMESTRE 2025
#Area de funciones
def mostrarProd(lista):
     marca = input("Ingrese la marca que desea ver (Logitech/AMD/Acer/LG/Corsair): ").lower()
     for producto in lista:
        if producto[2].lower() == marca:
            print("Productos disponibles:", producto)

def agrProd(lista):
    prod = input("Ingrese el nombre del producto: ")
    cat = input("Ingrese la categoría del producto: ")
    marca = input("Ingrese la marca del producto: ")
    mod = input("Ingrese el modelo del producto: ")
    est = input("Ingrese el estado (Lista/Oferta): ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    suc = input("Ingrese la sucursal: ")
    prodnuevo = [prod, cat, marca, mod, est, precio, stock, suc]
    lista.append(prodnuevo)
    print("Producto agregado con éxito")
    return lista

def actStock(lista):
    for i in lista:
        print(i)
    print()
    opcion = (input("Ingrese el producto que desea cambiar: "))
    for prod in lista:
        if prod[0].lower() == opcion.lower():
            stocknuevo = int(input("Ingrese el nuevo stock: ")) 
            prod[6] = stocknuevo
            print("La opcion", opcion, "fue cambiada con exito a: ",stocknuevo)
            return lista

def actPrecio(lista):
    porcentaje = float(input("Ingrese el porcentaje de aumento (sin el '%'): "))
    for prod in lista:
        aumento = prod[5] * (porcentaje / 100) 
        prod[5] = prod[5] + aumento  
    print("Precios actualizados con ", porcentaje,"de aumento")
    return lista

def lisCat(lista):
    categoria = input("Ingrese la categoria que desea ver (Perifericos/Monitores/Componentes/Accesorios/Computadoras): ").lower()
    for prod in lista:
        if prod[1].lower() == categoria:
            print("Productos disponibles:", prod)

def lisSuc(lista):
    sucursal = input("Ingrese la sucursal que desea ver (CABA/Adrogue/Temperley): ").lower()
    for i in lista:
        if i[7].lower() == sucursal :
            print("Productos disponibles en ", sucursal ,":", i)

def elim(lista):
    for i in lista:
        print(i)
    print()
    prod = input("Ingrese el producto que desea eliminar: ").lower()
    for b in lista:
        if b[0].lower() == prod:
            lista.remove(b)
            print("Se borro correctamente ",prod)
            return lista
    else: print("Producto no existente.")

def mostrarProm(lista):
    iterador = 0
    suma = 0
    opcion = input("Que categoria desea calcular el promedio?: ")
    for i in lista:
        if i[1] == opcion:
            suma = suma + i[5]
            iterador = iterador + 1
    promedio = suma / iterador
    print("Su promedio es: ", promedio)
    return promedio

#Programa principal
menu="""
1. Mostrar productos disponibles de una marca
2. Agregar un producto
3. Actualizar el estado de stock de un producto 
4. Actualizar precio de todos los productos 
5. Listar por categoria de un producto. (Perifericos/Componente/Monitor, etc.)
6. Listar productos de una sucursal. El usuario debera ingresar la sucursal (CABA/Temperley/Adrogue)
7. Eliminar un producto 
8. Mostrar promedio de precio de una categoria
9. Salir
"""

Productos = [
    ["Mouse Inalambrico", "Perifericos", "Logitech", "Logitech g309", "Oferta", 1500, 30, "CABA"],
    ["Teclado Mecánico", "Perifericos", "Logitech", "Logitech g413", "Lista", 3000, 28, "CABA"],
    ["Monitor 24 pulgadas", "Monitores", "LG", "LG 24MP88HV-S", "Lista", 12000, 20, "Adrogue"],
    ["Laptop Gamer", "Computadoras", "Acer", "Acer Predator Helios 300", "Lista", 80000, 9, "Adrogue"],
    ["Auriculares Inalambricos", "Perifericos", "Acer", "Acer WH-1000XM4", "Lista", 4000, 23, "CABA"],
    ["Disco Solido", "Componentes", "Corsair", "Corsair 480GB", "Oferta", 7000, 50, "CABA"],
    ["Tarjeta Gráfica", "Componentes", "AMD", "RX 6500 XT 8GB", "Oferta", 35000, 12, "Temperley"],
    ["Fuente de Poder", "Componentes", "Corsair", "Corsair RM750x", "Lista", 10000, 25, "Temperley"],
    ["Procesador", "Componentes", "AMD", "Ryzen 7 5700F", "Lista", 15000, 10, "Adrogue"],
    ["PC Gamer Armada", "Computadoras", "AMD", "Ryzen 5 3600G 16GB", "Oferta", 50000, 5, "CABA"],
    ["Cable HDMI", "Accesorios", "LG", "LG Cable HDMI", "Oferta", 500, 100, "CABA"],
    ["Mouse Pad", "Accesorios", "Logitech", "Logitech G440", "Oferta", 1600, 80, "Adrogue"],
    ["Soporte para Monitor", "Monitores", "LG", "LG Soporte para Monitor", "Lista", 2000, 40, "CABA"],
    ["Webcam HD", "Perifericos", "Logitech", "Logitech C920", "Lista", 4300, 30, "Temperley"],
    ["Microfono USB", "Perifericos", "Corsair", "Corsair Void Elite", "Lista", 1800, 35, "Temperley"],
    ["Soporte Auriculares", "Accesorios", "Corsair", "Corsair Soporte para Auriculares", "Oferta", 900, 60, "CABA"],
    ["Teclado de Membrana", "Perifericos", "Logitech", "Logitech K120", "Oferta", 1000, 70, "CABA"],
    ["Joystick", "Perifericos", "Logitech", "Logitech F310", "Lista", 2000, 55, "Adrogue"],
    ["Cable de Red", "Accesorios", "Acer", "Acer Cable de Red", "Lista", 300, 120, "Adrogue"],
    ["Memoria RAM", "Componentes", "Corsair", "Corsair Vengeance LPX 16GB", "Oferta", 5000, 30, "Temperley"]
]

print("Bienvenido a Hardware Tagliani Store!")

print(menu)

opcion = int(input("Ingrese una opción del menú: "))

while opcion != 9:
    if opcion == 1:
        mostrarProd(Productos)
    elif opcion == 2:
        Productos = agrProd(Productos)
    elif opcion == 3:
        actStock(Productos)
    elif opcion == 4:
        actPrecio(Productos)
    elif opcion == 5:
        lisCat(Productos)
    elif opcion == 6:
        lisSuc(Productos)
    elif opcion == 7:
        elim(Productos)
    elif opcion == 8:
        mostrarProm(Productos)
    else:
        print("Opción no válida")
    print(menu)
    opcion = int(input("Ingrese una opción: "))

print("Gracias por su visita")