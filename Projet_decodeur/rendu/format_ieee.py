from non_entiers import *
from entiers import *

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
def exposant(decimal):
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
    """
    Trouve la mantisse associé au format IEEE 754./

    Paramètres
    ----------
    nb : float
        Nombre décimal à convertir.

    Retour
    ------
    list[int]
        Liste des bits de la mantisse
    """
    binaire = fractionnaire_dec_vers_bin(nb,24)
    bin_decimal = binaire["enti"]+binaire["frac"] + [0]*23
    return bin_decimal[1:24]


#Instruction 31
def dec_vers_ieee(n):
    ieee = {}

    # ----- SIGNE -----
    if n < 0:
        ieee['sign'] = 1
        n = -n
    else:
        ieee['sign'] = 0

    # ----- CAS ZERO -----
    if n == 0:
        ieee['expo'] = [0] * 8
        ieee['mant'] = [0] * 23
        return ieee

    # ----- NORMALISATION -----
    e = 0
    m = n

    # Ajuster pour avoir 1 ≤ m < 2
    while m >= 2:
        m /= 2
        e += 1

    while m < 1:
        m *= 2
        e -= 1

    # ----- EXPOSANT BIAISÉ -----
    exposant_biais = e + 127

    expo_bits = []
    valeur = exposant_biais

    for i in range(8):
        expo_bits.insert(0, valeur % 2)
        valeur //= 2

    ieee['expo'] = expo_bits

    # ----- MANTISSE -----
    mantisse = []
    fraction = m - 1  # on enlève le 1 implicite

    for i in range(23):
        fraction *= 2
        bit = int(fraction)
        mantisse.append(bit)
        fraction -= bit

    ieee['mant'] = mantisse

    return ieee



#Instruction 32
def ieee_vers_dec(ieee):
    sign = ieee['sign']
    expo = ieee['expo']
    mant = ieee['mant']

    # ----- EXPOSANT -----
    exposant = 0
    for bit in expo:
        exposant = exposant * 2 + bit

    # ----- TEST ZERO (manuel) -----
    mantisse_nulle = True
    for bit in mant:
        if bit != 0:
            mantisse_nulle = False

    if exposant == 0 and mantisse_nulle:
        return 0

    e = exposant - 127

    # ----- MANTISSE -----
    m = 1
    puissance = 2

    for bit in mant:
        m += bit / puissance
        puissance *= 2

    valeur = m * (2 ** e)

    if sign == 1:
        valeur = -valeur

    return valeur


#Instruction 33
def afficher_ieee(ieee) :
    """
    Affiche la représentation IEEE 754 de manière lisible.

    Paramètres
    ----------
    ieee : dict
        Représentation IEEE 754.

    Retour
    ------
    str
        Représentation IEEE 754 avec des espaces.
    """
    s, e, m = ieee["sign"],ieee["expo"],ieee["mant"]
    char = str(s) + " "
    for elm in e+[" "]+m:
        char = char + str(elm)
    return char

    
    
#Instruction 34
# ===== TESTS dec_vers_ieee =====

assert dec_vers_ieee(5/8) == {
    'sign': 0,
    'expo': [0,1,1,1,1,1,1,0],
    'mant': [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
}

assert dec_vers_ieee(-100.25) == {
    'sign': 1,
    'expo': [1,0,0,0,0,1,0,1],
    'mant': [1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
}

assert dec_vers_ieee(0) == {
    'sign': 0,
    'expo': [0,0,0,0,0,0,0,0],
    'mant': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
}

# ===== TESTS ieee_vers_dec =====

assert ieee_vers_dec({
    'sign': 0,
    'expo': [0,1,1,1,1,1,1,0],
    'mant': [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
}) == 5/8

assert ieee_vers_dec({
    'sign': 1,
    'expo': [1,0,0,0,0,1,0,1],
    'mant': [1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
}) == -100.25

















