nums = input("Porfavor introduzca una secuencia de numeros separados por comas: ")

lista = []
lista = nums.split(",")
suma = 0
for i in (lista):
    suma += int(i)
print("La suma total de los numeros:", suma)