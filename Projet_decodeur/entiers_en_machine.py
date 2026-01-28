#fonction nécéssaire pour éxécuter les programmes : 
def lst_to_str(L):
    ch = ""
    for elm in L:
        ch = ch + str(elm)
    return ch
    

#instruction 17
def est_representable_bin(nb, b):
    if b <= 0:
        return False
    return 0 <= nb < 2**b

#instruction 18
def est_representable_bin_signe(n, b):
    min_val = -2**(b-1)
    max_val = 2**(b-1) - 1
    return min_val <= n <= max_val

#instruction 19
def est_representable_comp2(nb, b):
    if b <= 0:
        return False
    return -2**(b-1) <= nb < 2**(b-1)

#instruction 22
def bin_machine_vers_dec(bits):
    # Convertit une liste de bits (non signée) en entier décimal
    valeur = 0
    for bit in bits:
        valeur = valeur * 2 + bit
    return valeur

#instruction 23
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

#instruction 24
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

#instruction 25
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

