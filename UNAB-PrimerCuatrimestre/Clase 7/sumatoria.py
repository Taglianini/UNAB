#Area de funciones
def factorial(n):
     if n==1:
          return 1
     else:
          return n * factorial(n-1)
#Programa Principal
x=int(input("Ingrese un numero entero positivo: "))
print(factorial(x)) 
