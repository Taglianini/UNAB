Notas_alumnos = [["Tomas", 9], ["Ricardo", 9], ["Lautaro", 10], ["Ana", 1],["Agus", 2], ["Sofia", 3]]
print(Notas_alumnos[0])
print(Notas_alumnos)

Notas_alumnos.append(["Lucas", 7])
nom_alumno=input("Ingrese el nombre del alumno: ")
nota=int(input("Ingrese la nota del alumno: "))
Notas_alumnos.append([nom_alumno, nota])


print(Notas_alumnos)

print(len(Notas_alumnos))

print(["Tomas", 9] in Notas_alumnos)
Notas_alumnos[0] = ["Thomas", 10]
print(Notas_alumnos)