palabras = input("Escribe una palabra: ")   
vocales = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
cantv = 0
cantc = 0
for letra in palabras:
    if letra in vocales:
        cantv = cantv + 1
    elif letra == " ": 
        pass
    else:
        cantc = cantc + 1
print("Vocales: ", cantv, "Consonantes:", cantc)