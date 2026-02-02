def bin_vers_dec(b):
    n = 0
    for i in range(len(b)):
        n += b[i] * 2**(len(b) - i - 1)
    return n


def dec_vers_bin(n):
    if n == 0:
        return [0]
    b = []
    while n > 0:
        b.append(n % 2)
        n = n // 2
    return b[::-1]


def hex_vers_dec(h):
    n = 0
    puissance = 0
    for i in range(len(h) - 1, -1, -1):
        elm = h[i]

        if '0' <= elm <= '9':
            chiffre = ord(elm) - ord('0')
        elif 'A' <= elm <= 'F':
            chiffre = ord(elm) - ord('A') + 10
        elif 'a' <= elm <= 'f':   
            chiffre = ord(elm) - ord('a') + 10
        else:
            return None

        n += chiffre * (16 ** puissance)
        puissance += 1

    return n


def hex_vers_bin(h):
    n = hex_vers_dec(h)
    if n == 0:
        return [0]
    b = []
    while n > 0:
        b.append(n % 2)
        n = n // 2
    return b[::-1]


def bin_vers_chaine(b):
    c = ""
    for elm in b:
        c += str(elm)
    return c


def fractionnaire_bin_vers_dec(b):
    n = 0
    for i in range(len(b)):
        n += b[i] * 2**-(i + 1)
    return n


def est_representable_bin_signe(n, b):
    min_val = -2**(b - 1)
    max_val = 2**(b - 1) - 1
    return min_val <= n <= max_val



def forme_normalisée(d) :
    if d < 0 :
        return (0 , dec_vers_bin(d), fractionnaire_dec_vers_bin(d, 16))
    if d < 0 :
        return (1 , dec_vers_bin(-d), fractionnaire_dec_vers_bin(-d, 16))

def afficher_ieee(ieee) :
    return ieee_vers_dec(ieee)

