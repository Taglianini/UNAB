nombre = input("Ingrese su nombre: ")
antiguedad=int(input("Ingrese su antiguedad: "))
sueldo=float(input("Ingrese su sueldo: "))

print("Hola", nombre, "su antiguedad es de", antiguedad, "años y su sueldo ahora es", sueldo)
sueldonuevo = float(input("Ingrese porcentaje de aumento: "))
print("Su sueldo ahora es", sueldo * (1 + sueldonuevo / 100))