#Instruction 28
def forme_normalisee(s,e,m):


#Instruction 29
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


#Instruction 30
def mantisse(x):
    s, e, m = forme_normalisee(x)
    return m


#Instruction 31
def dec_vers_ieee(x):
    def dec_vers_ieee(x):
    s, e, m = forme_normalisee(x)
    return {
        "signe": s,
        "exposant": exposant(x),
        "mantisse": m
    }


#Instruction 32
def ieee_vers_dec(ieee):
    # Convertit un nombre IEEE 754 en décimal
    s = ieee["sign"]  # bit de signe
    expo = ieee["expo"]  # exposant
    mant = ieee["mant"]  # mantisse


#Instruction 33
def afficher_ieee():
    
    
#Instruction 34
def tests_ieee():
    # Tests automatiques des conversions IEEE
    assert round(ieee_vers_dec(dec_vers_ieee(1.0)), 5) == 1.0
    assert round(ieee_vers_dec(dec_vers_ieee(2.5)), 5) == 2.5
