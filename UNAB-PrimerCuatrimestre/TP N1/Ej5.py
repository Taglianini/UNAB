def invertir_lista(lista):
    lista_invertida = []
    for apellido in lista:
        lista_invertida.insert(0, apellido)
    return lista_invertida

lista = ["Julius", "Perez", "Thoms"]

print("Lista invertida:", invertir_lista(lista))

