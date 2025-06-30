#Dada una lista de datos de los clientes de un Gym con la siguiente estructura:
#clientes = [id, apellido, edad, dni, sexo (F/M/NB), plan (brazos, piernas, espalda), estado (activo/inactivo), 
# apellido_entrenador, rutina (full/medio/básico), precio]
#Consignas:
#1) Definir una función que calcule el porcentaje de clientes del sexo masculino (sexo = "M") que asisten al Gym.
#2) Definir una función que determine qué entrenador ("Villalba" o "Soria") tiene más clientes a su cargo.

#AF
def porcentaje(clientes):
     totalcliente = len(clientes)
     promedio = 0

     for i in clientes:
          if i[4] == "M":
               promedio = promedio + 1
     porMasc = (promedio / totalcliente) * 100
     return porMasc

def entrenador(clientes):
     villalba = 0
     soria = 0
     for i in clientes:
          if i[8] == "Soria":
               soria = soria + 1
          else: villalba = villalba + 1
     if soria > villalba:
          print("Soria es el ganador con:", soria)
     else: print("Villalba es el ganador con:", villalba)            
     return clientes

#PP
clientes = [
[1, "Gómez", 25, "12345678", "M", "brazos", "activo", "Villalba", "full", 5000],
[2, "Pérez", 30, "87654321", "F", "piernas", "activo", "Soria", "medio", 4000],
[3, "López", 22, "45678912", "M", "espalda", "inactivo", "Villalba", "básico", 3000],
[4, "Martínez", 35, "98765432", "M", "brazos", "activo", "Soria", "full", 5000]
]

print("Porcentaje de M",porcentaje(clientes),"%")
print("Los clientes elijen mas a: ",entrenador(clientes))