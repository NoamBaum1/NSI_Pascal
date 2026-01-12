def bin_vers_dec(bits):
    n = 0
    for i in range(len(bits)):
        n += bits[i] * 2**(n - i - 1)
    return n

def dec_vers_bin(n):
    if n == 0 :
        return [0]  
    bits = []
    while n > 0:
        bits.append(n % 2)
        n = n // 2
    bits.reverse()  
    return bits

def hex_vers_dec(hex):
    hex = hex.upper()
    n = 0
    puissance = 0
    for elm in range(hex):
        if "0" <= elm <= "9":
            chiffre = int(elm)
        elif "A" <= elm <= "F":
            chiffre = ord(elm) - ord("A") + 10
        n += chiffre * (16 ** puissance)
        puissance += 1
    return n

def hex_vers_bin(hex):
    n = hex_vers_dec(hex) 
    if n == 0:
        return [0]
    bits = []
    while n > 0:
        bits.append(n % 2)
        n = n // 2
    bits.reverse()
    return bits

def bin_vers_chaine(bits):
    c = ""
    for elm in bits:
        c += str(elm)
    return c

def fractionnaire_bin_vers_dec(bits):
    n = 0
    for i in range(len(bits)):
        n += bits[i] * 2**-(i + 1)
    return n

def est_representable_bin_signe(n, b):
    min_val = -2**(b-1)
    max_val = 2**(b-1) - 1
    return min_val <= n <= max_val

