#Nos contratan para realizar un sistema para una clínica de salud de Quilmes. Se conoce: Código del Paciente 
# Apellido Edad DNI Obra Social, Código del Médico que lo atendió, Fecha del turno, Hora del turno 
# Requisitos:
# Función para cargar pacientes: Crear una lista con información de los pacientes.
# La carga finaliza cuando se ingresa el código del paciente "zzz".
#Menú de opciones:
# 1. Imprimir la lista de pacientes que atenderá un determinado médico (ingresando su código).
# 2. Dar turno a un paciente (agregar datos de un nuevo paciente).
# 3. Modificar la hora del turno de un paciente.
# 4 .Imprimir la lista de pacientes de una Obra Social (ingresando su nombre).
# 5. Salir.
#Desarrollo del Programa: Primero: Cargar los datos de la clínica. Luego: Mostrar el menú de opciones
#Cada opción del menú debe implementarse con funciones.

#Area de funciones
def imp(Pacientes):
     medico = int(input("Ingrese el codigo del medico (8739 Azaro/ 6666 Fernandez): "))
     for i in Pacientes:
          if i[5] == medico:
               print(i)

def turno(Pacientes):
     cod = int(input("Ingrese el codigo del paciente: "))
     ape = input("Ingrese el apellido del paciente: ")
     edad = int(input("Ingrese edad del paciente: "))
     dni = int(input("Ingrese el DNI: "))
     ob = input("Ingrese la obra social del paciente: ")
     fecha = input("Ingrese la fecha del turno que desea")
     hora = input("Ingrese la hora del turno que desea: ")
     paciente = [cod, ape, edad, dni, ob, fecha, hora]
     Pacientes.append(paciente)
     print("Paciente agregado con exito ", paciente)
     return Pacientes

def modH(Pacientes):
     dni = int(input("Ingrese su DNI: "))
     for i in Pacientes:
          if i[3] == dni:
               print("Su horario actual es: ", i[7])
               hornuev = input("Ingrese su horario deseado: ")
               i[7] = hornuev
               print("Su horario se cambio con exito a: ",  hornuev)
     return Pacientes

def lisOb(Pacientes):
     ob = input("Ingrese la obra social (OSDE/OSECAC): ")
     for i in Pacientes:
          if i[4] == ob:
               print(i)

#Programa Principal
Pacientes = [
     [3234 , "Lopez", 28, 4512390, "OSDE", 8739, "11-9", "10:30" ],
     [1698 , "Juarez", 22, 31213981, "OSECAC", 6666, "11-9", "16:30" ],
     [3234 , "Rodriguez", 38, 1510230, "OSDE", 8739, "12-9", "9:30" ],
     [2153 , "Jerez", 38, 1510230, "OSECAC", 8739, "15-9", "8:30" ],
     [7777 , "Tagliani", 21, 45480676, "OSDE", 6666, "13-9", "19:30" ]
]

menu="""
1. Imprimir la lista de pacientes que atenderá un determinado médico (ingresando su código).
2. Dar turno a un paciente (agregar datos de un nuevo paciente).
3. Modificar la hora del turno de un paciente.
4 .Imprimir la lista de pacientes de una Obra Social (ingresando su nombre).
5. Salir.
"""

print(menu)
opcion = int(input("Ingrese una opcion del menu: "))
while opcion != 5:
     if opcion == 1:
          imp(Pacientes)
     elif opcion == 2:
          turno(Pacientes)
     elif opcion == 3:
          modH(Pacientes)
     elif opcion == 4:
          lisOb(Pacientes)
     else: 
          print("Ingrese una opcion valida")
     print(menu)
     opcion = int(input("Ingerse una opcion del menu: "))

print("Gracias por su visita")
