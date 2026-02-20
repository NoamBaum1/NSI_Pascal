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
def exposant(x):
    """
    Calcule les 8 bits de l'exposant IEEE 754 simple précision.

    Paramètres
    ----------
    x : float
        Nombre décimal à convertir.

    Retour
    ------
    list[int]
        Liste de 8 bits correspondant à l’exposant biaisé (biais = 127).
    """
    if x == 0:
        # Pour 0, exposant = 0
        return [0]*8

    # Calculer l'exposant en base 2
    import math
    e = int(math.floor(abs(x)).bit_length() - 1 if abs(x) >= 1 else math.floor(math.log2(abs(x))))
    
    # Biais IEEE 754 simple précision
    e_biais = e + 127

    # Conversion en 8 bits
    bits = []
    for i in range(8):
        bits.insert(0, e_biais % 2)
        e_biais //= 2

    return bits


#Instruction 30
def mantisse(x):
    


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







