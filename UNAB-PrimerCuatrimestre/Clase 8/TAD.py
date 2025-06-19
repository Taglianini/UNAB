class Cancion:
    def __init__(self, titulo, duracion, genero, artista):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.artista = artista

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre} ({self.genero}, {self.duracion} min)"


class Artista:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"


class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def buscar_por_genero(self, genero):
        return [c for c in self.canciones if c.genero.lower() == genero.lower()]


# ----------- PROGRAMA PRINCIPAL -----------

# Crear artistas
artista1 = Artista("Coldplay", "Reino Unido")
artista2 = Artista("Shakira", "Colombia")

# Crear canciones
c1 = Cancion("Viva La Vida", 4.0, "Rock", artista1)
c2 = Cancion("Yellow", 4.2, "Rock", artista1)
c3 = Cancion("Waka Waka", 3.5, "Pop", artista2)

# Crear playlist y agregar canciones
mi_playlist = Playlist("Mi música favorita")
mi_playlist.agregar_cancion(c1)
mi_playlist.agregar_cancion(c2)
mi_playlist.agregar_cancion(c3)

# Mostrar playlist con un print simple y un ciclo
print(f"Playlist: {mi_playlist.nombre}")
print("Canciones:")
for cancion in mi_playlist.canciones:
    print(cancion)

# Buscar canciones por género y mostrar
print("\nCanciones de género 'Rock':")
for cancion in mi_playlist.buscar_por_genero("Rock"):
    print(cancion)

