#Instruction 28
def forme_normalisee(nb):
    """
    Décompose un nombre décimal en forme normalisée
    (signe, exposant, mantisse) pour le format IEEE 754.

    Paramètres
    ----------
    nb : float
        Nombre décimal à convertir.

    Retour
    ------
    tuple
        (signe, exposant, mantisse)
        signe : bit de signe (0 ou 1)
        exposant : liste des 8 bits de l’exposant biaisé
        mantisse : liste des bits de la mantisse
    """
    if nb <= 0:
        signe = 0
    else:
        signe = 1
    return(signe,exposant(nb),mantisse(nb))


#Instruction 29
def exposant(nb):
    """
    Calcule les 8 bits de l'exposant IEEE 754 simple précision.

    Paramètres
    ----------
    nb : float
        Nombre décimal à convertir.

    Retour
    ------
    list[int]
        Liste de 8 bits correspondant à l’exposant biaisé (biais = 127).
    """
    nb = fractionnaire_dec_vers_bin(decimal,24)
    if len(nb["enti"]) == 1 and nb["enti"][0]==0 :
        exp = -1
        while nb["enti"][0] == 1:
            nb["enti"] = nb["enti"][1:]
            exp -= 1
        return [0] * (8 - len(dec_vers_bin(exp+127))) + dec_vers_bin(exp+127)
    else:
        return [0] * (8 - len(dec_vers_bin(len(nb["enti"])+126))) + dec_vers_bin(len(nb["enti"])+126)


#Instruction 30
def mantisse(nb):
    binaire = fractionnaire_dec_vers_bin(nb,24)
    bin_decimal = binaire["enti"]+binaire["frac"] + [0]*23
    return bin_decimal[1:24]


#Instruction 31
def dec_vers_ieee(x):
    """
    Convertit un nombre décimal en représentation IEEE 754
    simple précision (32 bits).

    Paramètres
    ----------
    x : float
        Nombre décimal à convertir.

    Retour
    ------
    dict
        Dictionnaire contenant :
        - 'signe' : bit de signe
        - 'exposant' : liste des 8 bits d’exposant
        - 'mantisse' : liste des 23 bits de mantisse
    """
    s, e, m = forme_normalisee(x)
    return {
        "signe": s,
        "exposant": e
        "mantisse": m
    }


#Instruction 32
def ieee_vers_dec(ieee):
    """
    Convertit une représentation IEEE 754 simple précision
    en nombre décimal.

    Paramètres
    ----------
    ieee : dict
        Dictionnaire contenant :
        - 'signe' : bit de signe
        - 'exposant' : liste des 8 bits
        - 'mantisse' : liste des 23 bits

    Retour
    ------
    float
        Valeur décimale correspondante.
    """
    # Convertit un nombre IEEE 754 en décimal
    s = ieee["sign"]  # bit de signe
    expo = ieee["expo"]  # exposant
    mant = ieee["mant"]  # mantisse


#Instruction 33
def afficher_ieee(ieee) :
    """
    Affiche la valeur décimale correspondant
    à une représentation IEEE 754.

    Paramètres
    ----------
    ieee : dict
        Représentation IEEE 754.

    Retour
    ------
    float
        Valeur décimale correspondante.
    """
    return ieee_vers_dec(ieee)

    
    
#Instruction 34
def tests_ieee():
    """
    Effectue des tests automatiques pour vérifier
    la validité des conversions IEEE 754.
    """
    # Tests automatiques des conversions IEEE
    assert round(ieee_vers_dec(dec_vers_ieee(1.0)), 5) == 1.0
    assert round(ieee_vers_dec(dec_vers_ieee(2.5)), 5) == 2.5








