#Area de funciones
def promedio(num):
     suma = num[0] + num[1] + num[2] + num[3]
     suma = suma / 4
     return suma

#Programa Principal
numeros = [4, 2, 8, 6]
resultado = promedio(numeros)
print("El promedio es:", resultado)