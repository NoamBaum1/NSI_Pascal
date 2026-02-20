from entier import *
from non_entier import *
from format_ieee import *
from entier_en_machine import *

#INSTRUCTIONS 35 
def menu_saisie():
    # ----- Choix de la base -----
    base = ""
    while base not in ["1", "2", "3", "4"]:
        print("Choisir une base :")
        print("1 - Décimal")
        print("2 - Binaire")
        print("3 - Octal")
        print("4 - Hexadécimal")
        base = input("Votre choix : ")
        if base not in ["1","2","3","4"]:
            print("Erreur : choix invalide")

    # ----- Saisie du nombre -----
    while True:
        n = input("Saisir le nombre : ")

        # Décimal
        if base == "1" and n.lstrip('-').isdigit():
            return int(n)

        # Binaire
        elif base == "2":
            valide = True
            for c in n:
                if c not in "01":
                    valide = False
            if valide and n != "":
                return int(n, 2)

        # Octal
        elif base == "3":
            valide = True
            for c in n:
                if c not in "01234567":
                    valide = False
            if valide and n != "":
                return int(n, 8)

        # Hexadécimal
        elif base == "4":
            valide = True
            for c in n.upper():
                if c not in "0123456789ABCDEF":
                    valide = False
            if valide and n != "":
                return int(n, 16)

        print("Erreur : saisie invalide pour cette base, recommencez")


#INSTRUCTIONS 36
def menu_conversion():
    print("=== REPRESENTATIONS DES NOMBRES ===")

    n = menu_saisie()

    representations = {}

    # Signe
    if n < 0:
        representations['sign'] = 1
    else:
        representations['sign'] = 0

    representations['dec'] = n

    # Binaire
    representations['bin'] = dec_vers_bin(abs(n))

    # Hexadécimal
    representations['hex'] = dec_vers_hex(abs(n))

    # Complément à 2 sur 8 bits
    representations['comp2'] = dec_vers_comp2(n, 8)

    print("\nRESULTATS\n")

    print("Décimal :", representations['dec'])
    print("Binaire :", representations['bin'])
    print("Hexadécimal :", representations['hex'])
    print("Complément à 2 :", representations['comp2'])
