lectura = open("personas.txt", "r", encoding="utf-8")

lineas = lectura.readlines()
lista = []
for linea in lineas:
    lista.append(linea.split(";"))
lista1 = []
for i in lista:
    for j in i:
        lista1.append(j.split())
        
num = 0
menor = float('inf')
pos = 0
nombre = ""
for i in lista1:
    pos += 1
    for j in i:
        if j[0] == "1" or j[0] == "2" or j[0] == "3" or j[0] == "4" or j[0] == "5" or j[0] == "6" or j[0] == "7" or j[0] == "8" or j[0] == "9" or j[0] == "0":
            if num < int(j):
                num = int(j)
                posicion = pos -2
            if menor > int(j):
                menor = int(j)
                posicion1 = pos - 2
                

print("La persona mas mayor es",lista1[posicion][0], num)

print("La persona mas pequeña es",lista1[posicion1][0], menor)
