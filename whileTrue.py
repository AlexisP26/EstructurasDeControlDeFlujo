#1 BUSCAR PRECIO POR EL NOMBRE
menu = [
    ["Hamburguesa", 18000],
    ["Pizza", 25000],
    ["Tacos", 20000]
]
#Ejercicio:
#Usa while True para pedir al usuario un nombre de plato.
#Si lo encuentra, muestra el precio y usa break.
#Si no existe, imprime "No existe en el menú".

while True:
    nombre = input("ingrese el nombre del plato")
    encontrado = False 
    for plato in menu:
        if nombre.lower() == plato[0].lower():
            print ("precio", plato[1])
            encontrado = True
            break
    if encontrado == True:
        break
    else:
        print("el plato no fue encontrado")    

#2 TOTAL VENTAS
pedidos = [
    ["Mesa 1", 45000],
    ["Mesa 2", 30000],
    ["Mesa 3", 0]
]
#
#Recorre con while True sumando los valores.
#Si el valor es 0 usa continue (no lo sumes).
#Cuando termine la matriz usa break.
#Muestra el total vendido.

i = 0
total = 0
while True:
    if i>= len(pedidos):
        break
    valor = pedidos[i][1]
    if valor == 0:
        i = i + 1
        continue
    total = total + valor
    i = i + 1
    print(total)

#3Control de stock con continue
inventario = [
    ["Pan", 10],
    ["Carne", 0],
    ["Queso", 5]
]
#Recorre con while True.
#Si la cantidad es 0, usa continue.
#Si es mayor a 0, muestra que está disponible.
#Finaliza con break cuando termine la matriz.
i=0
while True:
    if i >= len(inventario):
        break
    cantidad = inventario[i][1]
    if cantidad == 0:
        i = i + 1
        continue
    print(inventario[i][0], inventario[i][1] )
    i = i + 1