#Instruction 14
def fractionnaire_dec_vers_bin(nb,p):
    """
    Convertit un nombre décimal (avec partie fractionnaire)
    en représentation binaire signée.

    Paramètres
    ----------
    nb : float
        Nombre décimal à convertir.
    p : int
        Nombre maximum de bits pour la partie fractionnaire.

    Retour
    ------
    dict
        Dictionnaire contenant :
        - 'sign' : 0 si le nombre est positif, 1 s'il est négatif
        - 'enti' : liste de bits représentant la partie entière
        - 'frac' : liste de bits représentant la partie fractionnaire
    """
    if nb>=0:
        signe = 0 
    else:
        signe = 1
    nb = abs(nb)
    nb_entier = int(nb//1)
    bits_entier = []
    if nb_entier == 0:
        bits_entier = [0]
    while nb_entier > 0:
        bits_entier.append(nb_entier % 2)
        nb_entier = nb_entier // 2  
    
    nb_decimal = nb - nb//1
    bits_decimal = []
    

    for i in range(p):
        
        nb_decimal = nb_decimal * 2
        
        if nb_decimal == 0.0:
            break
        bits_decimal.append(int(nb_decimal//1))
        nb_decimal = nb_decimal - nb_decimal//1
    
    return{"sign" : signe, "enti" : bits_entier[::-1], "frac" : bits_decimal}


# Instruction 15
def fractionnaire_bin_vers_dec(binaire):
    """
    Convertit un nombre en représentation binaire fractionnaire en décimal
    sans utiliser enumerate.
    binaire : dict avec 'sign', 'enti', 'frac'
    Retour
    ------
    float
        Valeur décimale correspondante.
    """
    s = binaire['sign']
    enti = binaire['enti']
    frac = binaire['frac']

    # Partie entière
    valeur = 0
    for bit in enti:
        valeur = valeur * 2 + bit

    # Partie fractionnaire
    puissance = 2  # commence à 2^-1
    for bit in frac:
        valeur += bit / puissance
        puissance *= 2

    # Appliquer le signe
    if s == 1:
        valeur = -valeur

    return valeur



# Instruction 16

# Tests fractionnaire_dec_vers_bin
assert fractionnaire_dec_vers_bin(0.375, 10) == {
    'sign': 0,
    'enti': [0],
    'frac': [0, 1, 1]
}

assert fractionnaire_dec_vers_bin(-127.0078125, 10) == {
    'sign': 1,
    'enti': [1,1,1,1,1,1,1],
    'frac': [0,0,0,0,0,0,1]
}

# Tests fractionnaire_bin_vers_dec
assert fractionnaire_bin_vers_dec({
    'sign': 0,
    'enti': [0],
    'frac': []
}) == 0

assert fractionnaire_bin_vers_dec({
    'sign': 0,
    'enti': [1,0,1],
    'frac': [1,0,0]
}) == 5.5

assert fractionnaire_bin_vers_dec({
    'sign': 1,
    'enti': [1,1,0,0,1,0,0],
    'frac': [0,1,0,1,0,1]
}) == -100.328125





