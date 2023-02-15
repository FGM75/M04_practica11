def comparar_numeros():
    num1 = float(input("Introdueix el primer número: "))
    num2 = float(input("Introdueix el segon número: "))

    if num1 > num2:
        print(num1, "és més gran que", num2)
    elif num1 < num2:
        print(num2, "és més gran que", num1)
    else:
        print(num1, "i", num2, "són iguals")
