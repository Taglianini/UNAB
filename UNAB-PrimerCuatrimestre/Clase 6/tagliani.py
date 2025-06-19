#Area de Funciones
def MasAntiguos15(lista):
     li = []
     for empleado in lista:
        if empleado[4] > 15:
            li.append(empleado)
     return li

def empleado_max(lista):
    max = -9999
    nombre = " "
    for i in lista:
        if i[3] > max:
            max = i[3]
            nombre = i[1]
    return nombre

def promedio(lista):
    suma=0
    for i in lista:
        suma=suma+i[3]
    p = suma / len(lista)
    return p 

def aumento(lista):
    for empleado in lista:
        antiguedad = empleado[4]
        if antiguedad >= 10:
            empleado[3] *= 1.15
        if antiguedad <= 15:
            empleado[3] *= 1.10
    return lista
#Programa principal
ListaEmpleados = [
    [101, "Gómez", "Vendedor", 50000, 1],
    [102, "Pérez", "Vendedor", 60000, 14],
    [103, "López", "Gerente", 55000, 20],
    [104, "Martínez", "CM", 48000, 5],
    [101, "Tagliani", "Capo", 50000, 30],
    [102, "Rodriguez", "Aseo", 60000, 26],
    [103, "Avila", "Reparacion", 55000, 18],
    [104, "Sanchez", "Vendedor", 50000, 5],
]
empleados_antiguos = MasAntiguos15(ListaEmpleados)
#for i in empleados_antiguos:
#    print(i)
aumentos = aumento(ListaEmpleados)
for i in aumentos:
    print(i)