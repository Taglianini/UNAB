Estudiantes=[]
for i in  range(1,4):
     apellido=input("Ingrese el apellido del alumno: ")
     nota1=float(input("Ingrese la primer nota: "))
     nota2=float(input("Ingrese la segunda nota: "))
     alumno=[apellido, nota1, nota2]
     Estudiantes.append(alumno)

for i in Estudiantes:
     print(i)