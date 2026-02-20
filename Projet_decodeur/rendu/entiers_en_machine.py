

#instruction 17
def est_representable_bin(nb, b):
    """
    Vérifie si un entier est représentable en b bits (non signé).

    Paramètres
    ----------
    nb : int
        Nombre entier à tester.
    b : int
        Nombre de bits disponibles.

    Retour
    ------
    bool
        True si nb est compris entre 0 et 2^b - 1,
        False sinon.
    """
    if b <= 0:
        return False
    return 0 <= nb < 2**b

#instruction 18
def est_representable_bin_signe(n, b):
    """
    Vérifie si un entier est représentable en b bits
    avec représentation binaire signée (bit de signe).

    Paramètres
    ----------
    n : int
        Nombre entier à tester.
    b : int
        Nombre total de bits (dont 1 bit de signe).

    Retour
    ------
    bool
        True si n est compris entre -2^(b-1) et 2^(b-1) - 1,
        False sinon.
    """
    min_val = -2**(b-1)
    max_val = 2**(b-1) - 1
    return min_val <= n <= max_val

#instruction 19
def est_representable_comp2(nb, b):
    """
    Vérifie si un entier est représentable en complément à 2
    sur b bits.

    Paramètres
    ----------
    nb : int
        Nombre entier à tester.
    b : int
        Nombre de bits disponibles.

    Retour
    ------
    bool
        True si nb est compris entre -2^(b-1) et 2^(b-1) - 1,
        False sinon.
    """
    if b <= 0:
        return False
    return -2**(b-1) <= nb < 2**(b-1)

#instruction 20

def addition_binaire_machine(a, binaire, b):
    """
    Effectue l'addition de deux nombres binaires
    sur une machine limitée à b bits.

    Paramètres
    ----------
    a : list[int]
        Premier nombre binaire.
    binaire : list[int]
        Deuxième nombre binaire.
    b : int
        Nombre de bits de la machine.

    Retour
    ------
    tuple
        (resultat, retenue_machine)
        resultat : liste de b bits correspondant au résultat tronqué.
        retenue_machine : bit de débordement (overflow).
    """
    resultat = []
    retenue = 0
    
    i = len(a) - 1
    j = len(binaire) - 1
    
    while i >= 0 or j >= 0:
        bit_a = a[i] if i >= 0 else 0
        bit_b = binaire[j] if j >= 0 else 0
        
        somme = bit_a + bit_b + retenue
        
        resultat.insert(0, somme % 2)
        retenue = somme // 2
        
        i -= 1
        j -= 1
    
    # retenue finale éventuelle
    if retenue:
        resultat.insert(0, retenue)
    
    # Retenue machine = bit qui déborde
    retenue_machine = 0
    if len(resultat) > b:
        retenue_machine = resultat[0]
        resultat = resultat[-b:]   # on garde b bits
    
    return resultat, retenue_machine

#instruction 21

def dec_vers_bin_machine(n, b):
    """
    Convertit un entier décimal en binaire
    sur un nombre fixe de b bits (non signé).

    Paramètres
    ----------
    n : int
        Nombre décimal à convertir.
    b : int
        Nombre de bits disponibles.

    Retour
    ------
    list[int]
        Liste de b bits représentant le nombre.
    """
    bits = [0] * b
    i = b - 1
    while n > 0 and i >= 0:
        bits[i] = n % 2
        n //= 2
        i -= 1
    return bits


#instruction 22
def bin_machine_vers_dec(bits):
    """
    Convertit un nombre binaire (non signé)
    en entier décimal.

    Paramètres
    ----------
    bits : list[int]
        Liste de bits représentant un nombre binaire.

    Retour
    ------
    int
        Valeur décimale correspondante.
    """
    # Convertit une liste de bits (non signée) en entier décimal
    valeur = 0
    for bit in bits:
        valeur = valeur * 2 + bit
    return valeur

#instruction 23
def dec_vers_bin_signe(n, b):
    """
    Convertit un entier décimal en représentation
    binaire signée sur b bits.

    Paramètres
    ----------
    n : int
        Nombre décimal à convertir.
    b : int
        Nombre total de bits (dont 1 bit de signe).

    Retour
    ------
    list[int]
        Liste de b bits représentant le nombre
        (bit de signe + valeur absolue).
    """
    # Déterminer le signe
    signe = 0 if n >= 0 else 1
    n = abs(n)

    # Conversion en binaire
    bits = []
    if n == 0:
        bits = [0]
    else:
        while n > 0:
            bits.insert(0, n % 2)
            n //= 2

    # Ajuster la longueur à b-1 bits (tronquer ou compléter à gauche)
    bits = bits[-(b-1):]       # tronquer si trop long
    while len(bits) < b - 1:   # compléter à gauche
        bits.insert(0, 0)

    return [signe] + bits



#instruction 24
def bin_signe_vers_dec(bits, b=None):
    """
    Convertit un nombre binaire signé en entier décimal.

    Paramètres
    ----------
    bits : list[int]
        Liste de bits représentant un nombre signé.
    b : int, optionnel
        Taille totale en bits (complète à gauche si nécessaire).

    Retour
    ------
    int
        Valeur décimale correspondante.
    """
    if not bits:
        return 0

    # Si on connaît la taille b, compléter à gauche pour avoir b bits
    if b is not None and len(bits) < b:
        bits = [0]*(b - len(bits)) + bits

    signe = bits[0]
    valeur = 0
    for bit in bits[1:]:
        valeur = valeur * 2 + bit

    return -valeur if signe == 1 else valeur



#instruction 25
def dec_vers_comp2(n, b):
    """
    Convertit un entier décimal en complément à 2
    sur b bits.

    Paramètres
    ----------
    n : int
        Nombre décimal à convertir.
    b : int
        Nombre de bits disponibles.

    Retour
    ------
    list[int]
        Représentation en complément à 2 sur b bits.
    """
    # Convertit un entier décimal en complément à 2 sur b bits
    bits = [0] * b

    # Cas d'un nombre positif ou nul
    if n >= 0:
        i = b - 1
        while n > 0:
            bits[i] = n % 2
            n = n // 2
            i -= 1
    else:
        # Cas d'un nombre négatif : on ajoute 2^b
        n = (2 ** b) + n
        i = b - 1
        while n > 0:
            bits[i] = n % 2
            n = n // 2
            i -= 1

    return bits

#instruction 26
def comp2_vers_dec(bits):
    """
    Convertit un nombre représenté en complément à 2
    en entier décimal.

    Paramètres
    ----------
    bits : list[int]
        Liste de bits en complément à 2.

    Retour
    ------
    int
        Valeur décimale correspondante.
    """
    if not bits:
        return 0

    # On s'assure que tous les éléments sont des bits 0 ou 1
    bits = [0 if b == 0 else 1 for b in bits]

    n_bits = len(bits)
    msb = bits[0]  # bit de poids fort

    # Nombre positif
    if msb == 0:
        valeur = 0
        for bit in bits:
            valeur = valeur * 2 + bit
        return valeur

    # Nombre négatif : complément à 2
    # Inversion des bits
    inverse = [1 - bit for bit in bits]

    # Ajout de 1
    retenue = 1
    for i in range(n_bits-1, -1, -1):
        somme = inverse[i] + retenue
        inverse[i] = somme % 2
        retenue = somme // 2

    # Conversion en décimal
    valeur = 0
    for bit in inverse:
        valeur = valeur * 2 + bit

    return -valeur



#instruction 27

# Tests est_representable_bin
assert est_representable_bin(15, 4) == True
assert est_representable_bin(15, 3) == False

# Tests est_representable_bin_signe
assert est_representable_bin_signe(-15, 5) == True
assert est_representable_bin_signe(-15, 4) == False
assert est_representable_bin_signe(-120, 9) == True
assert est_representable_bin_signe(-120, 8) == True
assert est_representable_bin_signe(-120, 7) == False

# Tests est_representable_comp2
assert est_representable_comp2(-15, 5) == True
assert est_representable_comp2(-16, 5) == True
assert est_representable_comp2(15, 5) == True
assert est_representable_comp2(16, 5) == False
assert est_representable_comp2(-10, 3) == False

# Tests addition_binaire_machine
assert addition_binaire_machine([1,0,1], [0,0,1], 3) == ([1,1,0], 0)
assert addition_binaire_machine([1,1,1], [0,0,1], 3) == ([0,0,0], 1)
assert addition_binaire_machine([1,1,1], [1,1,1], 3) == ([1,1,0], 1)

# Tests dec_vers_bin_machine
assert dec_vers_bin_machine(0, 4) == [0,0,0,0]
assert dec_vers_bin_machine(125, 8) == [0,1,1,1,1,1,0,1]
assert dec_vers_bin_machine(199, 8) == [1,1,0,0,0,1,1,1]

# Tests bin_machine_vers_dec
assert bin_machine_vers_dec([0,0,0,0]) == 0
assert bin_machine_vers_dec([0,0,1,1]) == 3
assert bin_machine_vers_dec([0,1,1,1,1,1,0,1]) == 125
assert bin_machine_vers_dec([1,1,0,0,0,1,1,1]) == 199

# Tests dec_vers_bin_signe
assert dec_vers_bin_signe(-5, 4) == [1,1,0,1]
assert dec_vers_bin_signe(5, 4) == [0,1,0,1]


# Tests bin_signe_vers_dec
assert bin_signe_vers_dec([1,1,0,1]) == -5
assert bin_signe_vers_dec([0,1,0,1]) == 5


# Tests dec_vers_comp2
assert dec_vers_comp2(5, 8) == [0,0,0,0,0,1,0,1]
assert dec_vers_comp2(-123, 8) == [1,0,0,0,0,1,0,1]
assert dec_vers_comp2(-123, 16) == [1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1]

# Tests comp2_vers_dec
assert comp2_vers_dec([0,0,0,0,0,1,0,5]) == 5
assert comp2_vers_dec([1,0,0,0,0,1,0,5]) == -123
assert comp2_vers_dec([1,0,0,0]) == -8






