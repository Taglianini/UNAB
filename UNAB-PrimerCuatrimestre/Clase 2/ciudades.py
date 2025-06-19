ciudades = ["Buenos HAires", "Madrid", "Real Sociedad"]

ciudades_nuevas = input("Escribe una nueva ciudad: ")

ciudades.append(ciudades_nuevas)

ciudades_viejas = ["Barcelona", "Valencia", "Bilbao"]

print(ciudades+ciudades_viejas)
print(len(ciudades+ciudades_viejas))

ciudades.remove("Madrid")
print ("Madrid" in ciudades)
print("Buenos Aires" in ciudades)
print(ciudades+ciudades_viejas)
print(len(ciudades+ciudades_viejas))


ciudades[0] = "Buenos Aires"
print(ciudades+ciudades_viejas)