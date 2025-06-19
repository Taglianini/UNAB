# Área de funciones
def sumastock(lista):
    cod = int(input('Ingrese el número de serie del producto que quiere actualizar: '))
    stock = int(input('Ingrese cuánto stock se sumó al producto: '))
    for i in lista:
        if i[0] == cod:
            i[4] = i[4] + stock

def l(lista):
    for i in lista:
        print(lista)

def liprodmarca(lista):
    marca = input('ingrese la marca del producto: ')
    for i in lista:
        if i[2] == marca:
            print(i)

def liprod(lista):
    for i in lista:
        if i[4] == 0:
            print('producto sin stock:', i)

# prog principal
productos = [
#numSerie - nombre - marca - tipo - cantidad - medida - precio -  sucursal
[101 , "mortadela" , "riosma" , "fiambre" , 50 , "kilo" , 5399.99 , "Quilmes"] ,
[102 , "salame tipo milan" , "riosma" , "fiambre" , 0, "kilo" , 6499.99 , "Bernal"] ,
[103 , "salamines" , "riosma" , "fiambre" , 35 , "kilo" , 8969.99 , "Berazategui"] ,
[201 , "jamon cocido" , "luvianka" , "fiambre" , 70 , "kilo" ,4699.99 , "Berazategui"] ,
[202 , "paleta de cerdo" , "luvianka" , "fiambre" , 100 , "kilo" , 3899.99 , "Bernal"]
]


#Programa Principal

menu ="""
1. Actualizar stock de un producto de la lista.
2. listar el producto mÃ¡s caro de una detrerminada sucursal
3. Mostrar lista de productos de una determinada marca por sucursal.
4. Listar los productos cuyo stock es 0
"""

print(menu)
op = int(input('Ingrese una opción del menú: '))

if op == 1:
    print(sumastock(productos))
elif op == 2:
    l(productos)
elif op == 3:
    liprodmarca(productos)
elif op == 4:
    liprod(productos)