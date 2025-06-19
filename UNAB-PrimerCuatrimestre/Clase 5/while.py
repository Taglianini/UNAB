lisp = []
lisn = []

n = int(input("ingresa un numero: "))

while n!=0:
    if n>0:
        lisp.append(n)
    else:
        lisn.append(n)
    n = int(input("ingresa otro numero: "))

print(lisp)
print(lisn)

