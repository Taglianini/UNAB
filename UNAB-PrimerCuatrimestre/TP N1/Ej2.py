def esta(lista, numero):
    for n in lista:
        if n == numero:
            return True
    return False

lista = [3, 6, 5, 8, 1]

n = int(input("Escribí un número para buscar en la lista: "))

print(esta(lista, n))


