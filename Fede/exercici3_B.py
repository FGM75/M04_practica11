def DeclaracioHisenda ():
    edat = input("Escriu la teva edat: ")
    edat = int(edat)
    ingresos = input("Escriu els teus ingresos: ")
    ingresos = int(ingresos)
    if (edat >= 18) and (ingresos > 1200):
        print("És necessari que facis la declaració d'hisenda")
    else:
        print("Encara no pots fe la declaració")
