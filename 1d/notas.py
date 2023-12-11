nota = int(input("Introduzca una nota: "))
nota1 = int(input("Introduzca una nota: "))
nota2 = int(input("Introduzca una nota: "))

if(nota < 4 and nota1 < 4 and nota2 < 4):
    print("La nota final es 0")

elif(nota > 4 and nota1 > 4 and nota2 > 4):
    notaf = nota * 0.3
    notaf1 = nota1 * 0.2
    notaf2 = nota2 * 0.5
    print("La nota final es",notaf + notaf1 + notaf2 )

else:
    print("La nota final es 2")