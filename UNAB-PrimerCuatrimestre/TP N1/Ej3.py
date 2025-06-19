def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

entrada = input("Escribí números separados por coma: ")
lista = [int(n) for n in entrada.split(",")]

print("La suma de la lista es:", sumar_lista(lista))

