#Instruction 28
def forme_normalisee(nb):
    if nb <= 0:
        signe = 0
    else:
        signe = 1
    return(signe,exposant(nb),mantisse(nb))


#Instruction 29
def exposant(x):
    """
    Retourne la liste des 8 bits de l'exposant IEEE 754 simple précision
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
    s, e, m = forme_normalisee(x)
    return {
        "signe": s,
        "exposant": e
        "mantisse": m
    }


#Instruction 32
def ieee_vers_dec(ieee):
    # Convertit un nombre IEEE 754 en décimal
    s = ieee["sign"]  # bit de signe
    expo = ieee["expo"]  # exposant
    mant = ieee["mant"]  # mantisse


#Instruction 33
def afficher_ieee(ieee) :
    return ieee_vers_dec(ieee)

    
    
#Instruction 34
def tests_ieee():
    # Tests automatiques des conversions IEEE
    assert round(ieee_vers_dec(dec_vers_ieee(1.0)), 5) == 1.0
    assert round(ieee_vers_dec(dec_vers_ieee(2.5)), 5) == 2.5






