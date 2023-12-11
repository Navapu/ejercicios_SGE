lista = []
while(True):
    num = int(input("Introduzca un numero: "))
    if num == 0:
        break
    else:
        lista.append(num)

buscar = int(input("\nIntroduzca un numero a buscar: "))

for i in range (len(lista)):
    if lista[i] == buscar:
        print("El numero seleccionado esta en la posicion", i)