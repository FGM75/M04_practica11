def mostra_missatge():
    noms = ['Ana', 'Maria', 'Pau', 'Lluc', 'Joan']
    nom = input("Si us plau, introdueix un nom: ")
    if nom in noms:
        if nom == 'Ana':
            print("Hola Ana, ets la millor!")
        elif nom == 'Maria':
            print("Hola Maria, com estàs?")
        elif nom == 'Pau':
            print("Hola Pau, què tal?")
        elif nom == 'Lluc':
            print("Hola Lluc, com va tot?")
        elif nom == 'Joan':
            print("Hola Joan, a què juguem avui?")
    else:
        print("Aquest nom no està a la llista.")
