#Definir una función que recibe una lista de palabras y retorna la de mayor longitud. 
def funcion(palabras):
    larga = palabras[0] 
    for i in palabras:
        if len(i) > len(larga):
            larga = i
    return larga


palabras = ["Universo", "Heimerdinger", "Gol", "Reus"]
print("La palabra mas larga es: ",funcion(palabras))

palabras.append("Otorrinonaringologia")
print(funcion(palabras))