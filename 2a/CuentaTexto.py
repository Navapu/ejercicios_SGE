cantidad = input("Introduzca un texto: ")

lista = cantidad.split(" ")
suma = 0
for i in lista:
    if i == "Python":
        suma += 1
print("La palabra Python sale una cantidad de veces de:", suma)