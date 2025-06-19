#Area de funciones
def calcular_porcentaje(alumnos):
    suma = 100 * aprobados / alumnos
    return suma

#Area de Programacion
cod_doc = input("ingrese su codigo de docente: ")
materia = input("ingrese la materia: ")
horas = int(input("ingrese la cantidad de horas: "))
alumnos = int(input("ingrese la cantidad de alumnos: "))
aprobados = int(input("ingrese la cantidad de alumnos aprobados: "))

docente = [cod_doc, materia, horas, alumnos, aprobados]
prom = calcular_porcentaje(alumnos)
print("El codigo de docente es:", cod_doc, "la materia es:", materia, "y el porcentaje de aprobados es: %", prom)

