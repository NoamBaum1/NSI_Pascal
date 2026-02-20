#INSTRUCTIONS 35 
def menu_saisie():
    print("Base du nombre :")
    print("1 - Décimal")
    print("2 - Binaire")
    print("3 - Octal")
    print("4 - Hexadécimal")

    base = input("Choix : ")

    while True:
        n = input("Saisie : ")

        # Décimal
        if base == "1" and n.lstrip('-').isdigit():
            return int(n)

        # Binaire
        if base == "2":
            valide = True
            for c in n:
                if c not in "01":
                    valide = False
            if valide and n != "":
                return int(n, 2)

        # Octal
        if base == "3":
            valide = True
            for c in n:
                if c not in "01234567":
                    valide = False
            if valide and n != "":
                return int(n, 8)

        # Hexadécimal
        if base == "4":
            valide = True
            for c in n.upper():
                if c not in "0123456789ABCDEF":
                    valide = False
            if valide and n != "":
                return int(n, 16)

        print("Erreur de saisie")
