num = int(input("Introduzca un numero: "))
num1 = int(input("Introduzca un numero: "))


while True:
    if num % num1 == 0:
        print("El MCD es:", num1)
        break
    elif(num % num1 != 0):
        while True:
            num = num % num1
            num, num1 = num1, num
            break