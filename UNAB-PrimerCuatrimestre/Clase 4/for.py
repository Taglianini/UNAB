lis = [1, 24, 7,28, 5, 12, 15, 6, 8, 10, 22]
print(lis)

lispares = [] 
lisimpares = []

for n in lis:
    if n % 2 == 0:
        lispares.append(n)
    else:
        lisimpares.append(n)
print()
print(lispares)
print()
print(lisimpares)
