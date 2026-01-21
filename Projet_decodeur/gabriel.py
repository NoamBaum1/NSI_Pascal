def oct_vers_dec(octal):
    valeur = 0
    puissance = len(octal) - 1
    for chiffre in octal:
        valeur += chiffre * (8 ** puissance)
        puissance -= 1
    return valeur

def dec_vers_oct(n):
    if n == 0:
        return [0]
    resultat = []
    while n > 0:
        resultat.insert(0, n % 8)
        n //= 8
    return resultat

def bin_vers_hex(binaire):
    decimal = bin_vers_entier(binaire)
    return dec_vers_hex(decimal)

def bin_vers_entier(binaire):
    valeur = 0
    puissance = len(binaire) - 1
    for bit in binaire:
        valeur += bit * (2 ** puissance)
        puissance -= 1
    return valeur

def hex_vers_chaine(hexa):
    caracteres = "0123456789ABCDEF"
    chaine = ""
    for chiffre in hexa:
        chaine += caracteres[chiffre]
    return chaine


def addition_binaire(a, b):
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

def dec_vers_bin_machine(n, b):
    bits = [0] * b
    i = b - 1
    while n > 0 and i >= 0:
        bits[i] = n % 2
        n //= 2
        i -= 1
    return bits

def mantisse(x):
    s, e, m = forme_normalisee(x)
    return m

def dec_vers_ieee(x):
    s, e, m = forme_normalisee(x)
    return {
        "signe": s,
        "exposant": exposant(x),
        "mantisse": m
    }
def convertir():
    valeur = saisir_nombre()
    resultat = {}

    if isinstance(valeur, int):
        resultat["decimal"] = valeur
        resultat["binaire"] = dec_vers_bin(valeur)
        resultat["hexadecimal"] = dec_vers_hex(valeur)
    else:
        resultat["decimal"] = valeur
        resultat["ieee"] = dec_vers_ieee(valeur)

    return resultat
