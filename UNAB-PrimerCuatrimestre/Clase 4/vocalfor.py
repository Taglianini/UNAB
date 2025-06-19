palabra = ["Universo"]
print(palabra)

lisvocales = [] 
lisconsonantes = []

for l in palabra:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        lisvocales.append(l)
    else:
        lisconsonantes.append(l)
print()
print(lisvocales)
print()
print(lisconsonantes)
