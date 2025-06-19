def sumar(lista):
    suma_positivos = 0
    suma_negativos = 0

    for numero in lista:
        if numero > 0:
            suma_positivos += numero
        elif numero < 0:
            suma_negativos += numero

    return suma_positivos, suma_negativos

lista = [4, -2, 7, -5, 3, -1, 6, -3]

positivos, negativos = sumar(lista)

print("Suma de positivos:", positivos)
print("Suma de negativos:", negativos)
