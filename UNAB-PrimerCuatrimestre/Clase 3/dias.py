#Area Funciones
def dia_corto(dia):
    if dia == 1:
        return "Lun"
    elif dia == 2:
        return "Mar"
    elif dia == 3:
        return "Mie"
    elif dia == 4:
        return "Jue"
    elif dia == 5:
        return "Vie"
    elif dia == 6:
        return "Sab"
    elif dia == 7:
        return "Dom"
    else:
        return "Error"
#Programa Principal 
dia = int(input("ingresa un dia de la semana (1-7): "))
print(dia_corto(dia)) 