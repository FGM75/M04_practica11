def ParellOSenar(numero1):
    numero1 = input("Indiqui un número ")
    numero1 = int(numero1)
    if numero1 % 2 != 0:
        print("{numero1} és senar".format(numero1=numero1))
    else:
        print("{numero1} és parell".format(numero1=numero1))