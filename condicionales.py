#1
menu = [
    ["Hamburguesa", 18000, True],
    ["Pizza", 25000, False],
    ["Perro caliente", 12000, True]
]
##Recorre la matriz y muestra únicamente los platos disponibles.
#Si un plato no está disponible, imprime: "El plato X no está disponible".

for plato in menu:
    if plato [2] == True:
        print(plato[0],"el plato esta disponible")
    else:
        print(plato[0],"el plato no esta disponible")
#2
menu = [
    ["Bandeja paisa", 30000],
    ["Arepa con queso", 8000],
    ["Sopa del día", 15000]
]

#Si el precio es mayor a 20000, aplica un descuento del 10%.
#Imprime el nombre del plato y su nuevo precio (si aplica descuento).

for plato in menu:
    nombre = plato[0]
    precio = plato[1]
    if precio > 20000:
        precio = precio - (precio*0.10)
        print(nombre, precio)
    else:
        print(nombre, precio)    

#3
menu = [
    ["Filete", 45000],
    ["Ensalada", 12000],
    ["Jugo natural", 7000]
]

#Clasifica cada plato como:
#"Económico" si es menor a 10000
#"Intermedio" entre 10000 y 30000
#"Premium" si es mayor a 30000

for plato in menu:
    precio = plato[1]
    if precio < 10000:
        print("economico")
    elif precio >= 10000 and precio <= 30000:
        print(" intermedio")
    elif precio > 30000:
        print("premium") 
    else:
        print("plato no encontrado")