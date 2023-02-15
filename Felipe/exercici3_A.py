import random

def endevinar_numero():
    numero_aleatori = random.randrange(101)
    intent = 0

    while intent < 5:
        numero_introduit = int(input("Indica un número entre 0 i 100: "))
        if numero_introduit == numero_aleatori:
            print("Molt bé! Has endevinat el número!")
            return
        elif numero_introduit < numero_aleatori:
            print("El número és més gran")
        else:
            print("El número és més petit")
        intent += 1

    print("Ho sento, no has endevinat el número. El número era", numero_aleatori)

