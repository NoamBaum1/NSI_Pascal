# Instructions 0
def afficher_binaire(bits):
     """
    Affiche et retourne une chaîne représentant un nombre binaire.

    Paramètres
    ----------
    bits : list[int]
        Liste de bits (0 et 1) représentant un nombre binaire.
        Le bit de poids faible est supposé être à la fin de la liste.

    Retour
    ------
    str
        Chaîne de caractères correspondant au nombre binaire,
        avec un espace ajouté tous les 4 bits.
    """
    nb = ""
    for i in range(len(bits)-1,-1,-1):
        nb = nb + str(bits[i])
        if i%4 == 0:
            nb = nb + " "
        print (nb)
    if nb[len(nb)-1]==" ":
        nb = nb[:len(nb)-1]
    return nb

    print(res)

# Instructions 1
def bin_vers_dec(bits):
    """
    Convertit un nombre binaire en nombre décimal.

    Paramètres
    ----------
    bits : list[int]
        Liste de bits (0 et 1) représentant un nombre binaire.

    Retour
    ------
    int
        Valeur décimale correspondante.
    """
    n = 0
    for i in range(len(bits)):
        n += bits[i] * 2**(len(bits)-i-1)
    return n


# Instructions 2
def dec_vers_bin(n):
    """
    Convertit un nombre décimal en binaire.

    Paramètres
    ----------
    n : int
        Nombre décimal à convertir.

    Retour
    ------
    list[int]
        Liste de bits représentant le nombre en base 2.
    """
    if n == 0 :
        return [0]  
    b = []
    while n > 0:
        b.append(n % 2)
        n = n // 2  
    return b[::-1]


# Instructions 3
def oct_vers_dec(octal):
    """
    Convertit un nombre octal en décimal.

    Paramètres
    ----------
    octal : list[int]
        Liste de chiffres (0 à 7) représentant un nombre en base 8.

    Retour
    ------
    int
        Valeur décimale correspondante.
    """
    valeur = 0
    puissance = len(octal) - 1
    for chiffre in octal:
        valeur += chiffre * (8 ** puissance)
        puissance -= 1
    return valeur


# Instructions 4
def dec_vers_oct(n):
    """
    Convertit un nombre décimal en octal.

    Paramètres
    ----------
    n : int
        Nombre décimal à convertir.

    Retour
    ------
    list[int]
        Liste de chiffres représentant le nombre en base 8.
    """
    if n == 0:
        return [0]
    resultat = []
    while n > 0:
        resultat.insert(0, n % 8)
        n //= 8
    return resultat

# Instructions 5
def hex_vers_dec(hexa):
    """
    Convertit un nombre hexadécimal en décimal.

    Paramètres
    ----------
    hexa : list[str | int]
        Liste contenant des chiffres hexadécimaux (0-9, A-F).

    Retour
    ------
    int
        Valeur décimale correspondante.
    """
    for i in range(len(hexa)):
        if hexa[i] == "A":
            hexa[i] = 10
        elif hexa[i] == "B":
            hexa[i] = 11
        elif hexa[i] == "C":
            hexa[i] = 12
        elif hexa[i] == "D":
            hexa[i] = 13
        elif hexa[i] == "E":
            hexa[i] = 14
        elif hexa[i] == "F":
            hexa[i] = 15
        else:
            hexa[i] = int(hexa[i])
    valeur = 0
    puissance = len(hexa) - 1
    for chiffre in hexa:
        valeur += chiffre * (16 ** puissance)
        puissance -= 1
    return valeur


# Instructions 6
def dec_vers_hex(dec):
    """
    Convertit un nombre décimal en hexadécimal.

    Paramètres
    ----------
    dec : int
        Nombre décimal à convertir.

    Retour
    ------
    list[str | int]
        Liste représentant le nombre en base 16 (0-9, A-F).
    """
    if dec == 0:
        return [0]
    hexa = []
    while dec > 0:
        hexa.insert(0, dec % 16)
        dec //= 16
    for i in range(len(hexa)):
        if hexa[i] == 10:
            hexa[i] = "A"
        elif hexa[i] == 11:
            hexa[i] = "B"
        elif hexa[i] == 12:
            hexa[i] = "C"
        elif hexa[i] == 13:
            hexa[i] = "D"
        elif hexa[i] == 14:
            hexa[i] = "E"
        elif hexa[i] == 15:
            hexa[i] = "F"

    return hexa


# Instructions 7
def bin_vers_hex(bits):
    """
    Convertit un nombre binaire en hexadécimal.

    Paramètres
    ----------
    bits : list[int]
        Liste de bits représentant un nombre binaire.

    Retour
    ------
    list[str | int]
        Représentation du nombre en base 16.
    """
    return dec_vers_hex(bin_vers_dec(bits))

# Instructions 8
def hex_vers_bin(bits):
    """
    Convertit un nombre hexadécimal en binaire.

    Paramètres
    ----------
    bits : list[str | int]
        Liste représentant un nombre en base 16.

    Retour
    ------
    list[int]
        Représentation du nombre en base 2.
    """
    return dec_vers_bin(hex_vers_dec(bits))

# Instructions 9
def bin_vers_chaine(b):
    """
    Transforme une liste de bits en chaîne de caractères.

    Paramètres
    ----------
    b : list[int]
        Liste de bits.

    Retour
    ------
    str
        Chaîne correspondant au nombre binaire.
    """
    c = ""
    for elm in b:
        c += str(elm)
    return c

# Instructions 10
def bin_vers_entier(bits):
    """
    Transforme une liste de bits en entier (sans conversion binaire).

    Paramètres
    ----------
    bits : list[int]
        Liste de bits.

    Retour
    ------
    int
        Entier correspondant à la concaténation des bits.
    """
    chaine = ""
    for bit in bits:
        chaine += str(bit)
    return int(chaine)


# Instructions 11
def hex_vers_chaine(hexa):
    """
    Transforme une liste hexadécimale en chaîne de caractères.

    Paramètres
    ----------
    hexa : list[str | int]
        Liste représentant un nombre en base 16.

    Retour
    ------
    str
        Chaîne hexadécimale correspondante.
    """
    car = ""
    for elm in hexa:
        car = car + str(elm)
    return car


# Instructions 12
def addition_binaire(a, b):
    """
    Effectue l'addition de deux nombres binaires.

    Paramètres
    ----------
    a : list[int]
        Premier nombre binaire.
    b : list[int]
        Deuxième nombre binaire.

    Retour
    ------
    list[int]
        Résultat de l'addition en binaire.
    """
    resultat = []
    retenue = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or retenue:
        bit_a = a[i] if i >= 0 else 0
        bit_b = b[j] if j >= 0 else 0

        somme = bit_a + bit_b + retenue
        resultat.insert(0, somme % 2)
        retenue = somme // 2

        i -= 1
        j -= 1

    return resultat

# Instructions 13

# Tests bin_vers_dec
assert bin_vers_dec([1, 0, 1, 0]) == 10
assert bin_vers_dec([1, 1, 1, 1]) == 15

# Tests dec_vers_bin
assert dec_vers_bin(10) == [1, 0, 1, 0]
assert dec_vers_bin(15) == [1, 1, 1, 1]

# Tests oct_vers_dec
assert oct_vers_dec([1, 2]) == 10      # 12₈ = 10₁₀
assert oct_vers_dec([1, 7]) == 15      # 17₈ = 15₁₀

# Tests dec_vers_oct
assert dec_vers_oct(10) == [1, 2]
assert dec_vers_oct(15) == [1, 7]

# Tests hex_vers_dec
assert hex_vers_dec([1, 'A']) == 26    # 1A₁₆ = 26₁₀
assert hex_vers_dec(['F']) == 15


# Tests bin_vers_hex
assert bin_vers_hex([1, 0, 1, 0]) == ['A']     # 1010₂ = A₁₆
assert bin_vers_hex([1, 1, 1, 1]) == ['F']

# Tests hex_vers_bin
assert hex_vers_bin(['A']) == [1, 0, 1, 0]
assert hex_vers_bin(['F']) == [1, 1, 1, 1]

# Tests bin_vers_chaine
assert bin_vers_chaine([1, 0, 1, 0]) == "1010"
assert bin_vers_chaine([1, 1, 1, 1]) == "1111"

# Tests bin_vers_entier
assert bin_vers_entier([1, 0, 1, 0]) == 1010
assert bin_vers_entier([1, 1, 1, 1]) == 1111

# Tests hex_vers_chaine
assert hex_vers_chaine([1, 'A']) == "1A"
assert hex_vers_chaine(['F']) == "F"

# Tests addition_binaire
assert addition_binaire([1, 0, 1, 0], [1, 1]) == [1, 1, 0, 1]  # 10 + 3 = 13
assert addition_binaire([1, 1, 1, 1], [1]) == [1, 0, 0, 0, 0]  # 15 + 1 = 16















