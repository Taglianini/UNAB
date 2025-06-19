productos = [
    #numSerie - nombre - marca - tipo - cantidad - medida - precio -  sucursal
    [101 , "mortadela" , "riosma" , "fiambre" , 50 , "kilo" , 5399.99 , "Quilmes"] ,
    [102 , "salame tipo milan" , "riosma" , "fiambre" , 0, "kilo" , 6499.99 , "Bernal"] ,
    [103 , "salamines" , "riosma" , "fiambre" , 35 , "kilo" , 8969.99 , "Berazategui"] ,
    [201 , "jamon cocido" , "luvianka" , "fiambre" , 70 , "kilo" ,4699.99 , "Berazategui"] ,
    [202 , "paleta de cerdo" , "luvianka" , "fiambre" , 100 , "kilo" , 3899.99 , "Bernal"]
]

#for p in productos: 
     #print(p)

for p in productos:
     print(p[0],p[1],p[2])
