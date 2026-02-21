from entiers import *
from non_entiers import *
from format_ieee import *
from entiers_en_machine import *

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
        if base == "1":
            valide = True
            for c in n:
                if c not in "0123456789.":
                    valide = False
            if valide and n != "":
                return float(n),base

        # Binaire
        elif base == "2":
            valide = True
            for c in n:
                if c not in "01":
                    valide = False
            if valide and n != "":
                return int(n),base

        # Octal
        elif base == "3":
            valide = True
            for c in n:
                if c not in "01234567":
                    valide = False
            if valide and n != "":
                return int(n),base

        # Hexadécimal
        elif base == "4":
            valide = True
            for c in n.upper():
                if c not in "0123456789ABCDEF":
                    valide = False
            if valide and n != "":
                n = [int(elm) if elm in "12334567890" else elm for elm in str(n)]
                n = hex_vers_dec(n)
                return n,base

        print("Erreur : saisie invalide pour cette base, recommencez")


#INSTRUCTIONS 36
def menu_conversion():
    """
    Fonction principale du programme.
    Lance le menu de saisie, construit un dictionnaire avec toutes les représentations du nombre
    et affiche les résultats.
    """
    print("=== REPRESENTATIONS DES NOMBRES ===\n")

    # Saisie du nombre par l'utilisateur
    n,base = menu_saisie()

    # Dictionnaire de stockage des représentations
    rep = {}
    rep['dec'] = n
    rep['sign'] = 0 if n >= 0 else 1

    # ----- CAS ENTIER -----
    if float(n) == float(int(n)) or base == 4:
          # Si n est un entier que n est bien un entier ou une liste en hexadécimal
        
        if base == "2":
            n = [int(elm) for elm in str(n)]
            n = bin_vers_dec(n)
        if base == "3":
            n = [int(elm) for elm in str(n)]
            n = oct_vers_dec(n)
        
        # Binaire
        rep['bin'] = afficher_binaire(dec_vers_bin(abs(n)))
        
        # Octal
        rep['oct'] = afficher_binaire(dec_vers_oct(abs(n)))
        
        # Hexadécimal
        rep['hex'] = afficher_binaire(dec_vers_hex(abs(n)))

        # Complément à 2 sur NB_BITS (par exemple 8 bits)
        rep['comp2'] = afficher_binaire(dec_vers_comp2(n, 8))

        # Affichage simple
        print("\nNombre entier détecté\n")
        print("Décimal        :", rep['dec'])
        print("Binaire        :", rep['bin'])
        print("Octal          :", rep['oct'])
        print("Hexadécimal    :", rep['hex'])
        print("Complément à 2 :", rep['comp2'])

    # ----- CAS NON ENTIER -----
    else:
        # Binaire fractionnaire (avec précision par défaut, ex: PRECISION = 10)
        nb = fractionnaire_dec_vers_bin(n, 10)
        s, e, f = nb["sign"],nb["enti"],nb["frac"]
        char = ""
        for elm in e+[","]+f:
            char = char + str(elm)
        
        
        rep['bin'] = char

        # Format IEEE 754 simple précision
        rep['ieee'] = afficher_ieee(dec_vers_ieee(n))

        # Affichage simple
        print("\nNombre non entier détecté\n")
        print("Décimal :", rep['dec'])
        print("Binaire :", rep['bin'])
        print("IEEE    :", rep['ieee'])
