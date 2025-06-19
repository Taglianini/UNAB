#Area de funciones 
def cargardatos():
    lista = []
    cod = int(input("Ingrese el código del producto: "))
    
    while cod != 9999:
        nom = input("Ingrese el nombre del producto: ")
        mar = input("Ingrese la marca del producto: ")
        tip = input("Ingrese el tipo de producto: ")
        stock = int(input("Ingrese el stock del producto: "))
        pre = float(input("Ingrese el precio del producto: "))
        suc = input("Ingrese el nombre de la sucursal: ")
        
        lis = [cod, nom, mar, tip, stock, pre, suc]
        lista.append(lis)
        
        cod = int(input("Ingrese el código de otro producto: "))
    
    return lista

def mascaro(lista):
    maxi = -999
    p = []
    suc=input("Ingrese la sucursal: ")
    prodcaro = -999
    for i in lista:
        if i[-1] == suc and i[-2]>maxi:
            maxi=i[-2]
            p=i
        return p
    
def prod0(lista):
    for i in lista:
        if i[4]==0:
            print('producto sin stock:',i)

#Programa principal
productos = [
    [101 , "mortadela" , "riosma" , "fiambre" , 50 , "kilo" , 5399.99 , "Quilmes"],
    [102 , "salame tipo milan" , "riosma" , "fiambre" , 0 , "kilo" , 6499.99 , "Bernal"],
    [103 , "salamines" , "riosma" , "fiambre" , 35 , "kilo" , 8969.99 , "Berazategui"],
    [201 , "jamon cocido" , "luvianka" , "fiambre" , 0 , "kilo" , 4699.99 , "Berazategui"],
    [202 , "paleta de cerdo" , "luvianka" , "fiambre" , 0 , "kilo" , 3899.99 , "Bernal"]
]

menu = """
Actualizar stock de un producto de la lista.
Listar el producto más caro de una determinada sucursal.
Mostrar lista de productos de una determinada marca por sucursal.
Listar los productos cuyo stock es 0
Salir
"""

print(menu)
opcion = int(input("Ingrese una opción del menú: "))
while opcion != 5:
    if opcion == 1: 
        print(cargardatos( ))
    elif opcion == 2:
        print(mascaro(productos))
    elif opcion == 3:
        print("Eligió la opción 3")
    elif opcion == 4:
          prod0(productos)
    else:
        print("Debe elegir una opción válida del menú.")
    opcion = int(input("Elija otra opción del menú: "))

print("Gracias por usar nuestro sistema.")
