#Instruction 28
def forme_normalisée(d) :
    if d < 0 :
        return (0 , dec_vers_bin(d), fractionnaire_dec_vers_bin(d, 16))
    if d < 0 :
        return (1 , dec_vers_bin(-d), fractionnaire_dec_vers_bin(-d, 16))


#Instruction 29
def exposant(x):


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
def afficher_ieee(ieee) :
    return ieee_vers_dec(ieee)

    
    
#Instruction 34
def tests_ieee():
    # Tests automatiques des conversions IEEE
    assert round(ieee_vers_dec(dec_vers_ieee(1.0)), 5) == 1.0
    assert round(ieee_vers_dec(dec_vers_ieee(2.5)), 5) == 2.5


