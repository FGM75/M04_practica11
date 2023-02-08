def MesGranMesPetit():
    num1 = input("Digues un número ")
    num1 = int(num1)
    num2 = input("Digues un altre número ")
    num2 = int(num2)
    if (num1 > num2):
        print("{num1} és més gran que {num2}".format(num1=num1, num2=num2))
    elif num1 == num2:
        print("")
    else:
        print("{num2} és més gran que {num1}".format(num1=num1, num2=num2))

