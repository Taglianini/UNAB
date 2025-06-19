datos = []
apellido = input("Ingrese un apellido: ")

while apellido != "zzz":
    dni = input("Ingrese el DNI: ")
    patente = input("Ingrese la patente: ")
    persona = [apellido, dni, patente]
    datos.append(persona)
    apellido = input("Ingrese un apellido: ")

print(datos)
