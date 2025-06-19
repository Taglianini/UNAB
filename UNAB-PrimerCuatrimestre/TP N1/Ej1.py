palabra = input("Ingrese una palabra: ")

lisvocales = [] 
lisconsonantes = []

for l in palabra:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u" or l == "A" or l =="E" or l == "I" or l == "O" or l == "U":
        lisvocales.append(l)
    else:
        lisconsonantes.append(l)
print()
print(lisvocales)
print()
print(lisconsonantes)