nequipo = input("Ingrese el nombre del equipo: ")
pjugados = int(input("Ingrese el número de partidos jugados: "))
pperdidos = int(input("Ingrese el número de partidos perdidos: "))
pganados = int(input("Ingrese el número de partidos ganados: "))
posicion = int(input("Ingrese la posición del equipo: "))

equipo = (nequipo, pjugados, pperdidos, pganados, posicion)
print(equipo)
print(equipo[0])
print(len(equipo))

