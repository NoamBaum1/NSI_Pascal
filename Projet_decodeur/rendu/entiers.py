# Instructions 0
def afficher_binaire(bits):
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
    n = 0
    for i in range(len(bits)):
        n += bits[i] * 2**(len(bits)-i-1)
    return n


# Instructions 2
def dec_vers_bin(n):
    if n == 0 :
        return [0]  
    b = []
    while n > 0:
        b.append(n % 2)
        n = n // 2  
    return b[::-1]


# Instructions 3
def oct_vers_dec(octal):
    valeur = 0
    puissance = len(octal) - 1
    for chiffre in octal:
        valeur += chiffre * (8 ** puissance)
        puissance -= 1
    return valeur


# Instructions 4
def dec_vers_oct(n):
    if n == 0:
        return [0]
    resultat = []
    while n > 0:
        resultat.insert(0, n % 8)
        n //= 8
    return resultat

# Instructions 5
def hex_vers_dec(hexa):
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
    return dec_vers_hex(bin_vers_dec(bits))

# Instructions 8
def hex_vers_bin(bits):
    return dec_vers_bin(hex_vers_dec(bits))

# Instructions 9
def bin_vers_chaine(b):
    c = ""
    for elm in b:
        c += str(elm)
    return c

# Instructions 10
def bin_vers_entier(bits):
    chaine = ""
    for bit in bits:
        chaine += str(bit)
    return int(chaine)


# Instructions 11
def hex_vers_chaine(hexa):
    car = ""
    for elm in hexa:
        car = car + str(elm)
    return car


# Instructions 12
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

# Instructions 13












