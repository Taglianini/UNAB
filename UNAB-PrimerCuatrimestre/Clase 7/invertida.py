#Area de funciones
def palindromo(p):
     if len(p) == 1 or len(p)==0:
        return True 
     else: 
        if p[0] == p[-1]:
           pal=p[1:-1]
           return palindromo(pal)
        else:
          return False
#Programa Principal 
palabra=(input("Ingrese una palabra: "))
print(palindromo(palabra)) 