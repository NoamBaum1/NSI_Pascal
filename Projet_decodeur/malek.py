def afficher_binaire(n):
    # Convertit un entier naturel en binaire et l'affiche avec des espaces
    bits = []

    # Cas particulier : si n vaut 0
    if n == 0:
        bits = [0]

    # Conversion décimal → binaire
    while n > 0:
        bits.insert(0, n % 2)  # on ajoute le reste au début
        n = n // 2             # division entière par 2

    # Construction de l'affichage avec groupes de 4 bits
    res = ""
    for i in range(len(bits)):
        res += str(bits[i])
        # Ajout d'un espace tous les 4 bits (sauf à la fin)
        if (len(bits) - i - 1) % 4 == 0 and i != len(bits) - 1:
            res += " "

    print(res)


def bin_machine_vers_dec(bits):
    # Convertit une liste de bits (non signée) en entier décimal
    valeur = 0
    for bit in bits:
        valeur = valeur * 2 + bit
    return valeur


def dec_vers_bin_signe(n, b):
    # Convertit un entier décimal en binaire signé sur b bits
    bits = [0] * b  # initialisation à 0

    # Si le nombre est négatif, le bit de signe vaut 1
    if n < 0:
        bits[0] = 1
        n = -n  # on travaille avec la valeur absolue

    # Conversion de la partie valeur
    i = b - 1
    while n > 0 and i > 0:
        bits[i] = n % 2
        n = n // 2
        i -= 1

    return bits


def bin_signe_vers_dec(bits):
    # Convertit un binaire signé en entier décimal
    signe = bits[0]  # bit de signe
    valeur = 0

    # Conversion de la partie valeur
    for bit in bits[1:]:
        valeur = valeur * 2 + bit

    # Si le signe est 1, le nombre est négatif
    if signe == 1:
        return -valeur
    return valeur


def dec_vers_comp2(n, b):
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


def exposant(x):
    # Retourne la liste des 8 bits de l'exposant IEEE 754

    if x == 0:
        return [0] * 8

    e = 0

    # Mise sous forme normalisée
    if abs(x) >= 1:
        while abs(x) >= 2:
            x = x / 2
            e += 1
    else:
        while abs(x) < 1:
            x = x * 2
            e -= 1

    # Ajout du biais IEEE
    e = e + 127

    # Conversion de l'exposant en binaire
    bits = []
    for _ in range(8):
        bits.insert(0, e % 2)
        e = e // 2

    return bits


def ieee_vers_dec(ieee):
    # Convertit un nombre IEEE 754 en décimal
    s = ieee["sign"]  # bit de signe
    expo = ieee["expo"]  # exposant
    mant = ieee["mant"]  # mantisse


def tests_ieee():
    # Tests automatiques des conversions IEEE
    assert round(ieee_vers_dec(dec_vers_ieee(1.0)), 5) == 1.0
    assert round(ieee_vers_dec(dec_vers_ieee(2.5)), 5) == 2.5


def menu_saisie():
    # Menu permettant de saisir un nombre dans différentes bases
    base = input("Choisir une base (10, 2, 8, 16) : ")

    if base == "10":
        return int(input("Entrer un entier décimal : "))

    if base == "2":
        n = input("Entrer un nombre binaire : ")
        while not all(c in "01" for c in n):
            n = input("Erreur, recommence : ")
        return n

    if base == "8":
        return input("Entrer un nombre octal : ")

    if base == "16":
        return input("Entrer un nombre hexadécimal : ")

    # Conversion de l'exposant
    e = 0
    for bit in expo:
        e = e * 2 + bit
    e = e - 127

    # Conversion de la mantisse
    m = 1
    puissance = 0.5
    for bit in mant:
        if bit == 1:
            m += puissance
        puissance /= 2

    return ((-1) ** s) * m * (2 ** e)
