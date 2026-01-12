def lst_to_str(L):
    ch = ""
    for elm in L:
        ch = ch + str(elm)
    return ch
    


def base_b_vers_dec(nb, b):
    if type(nb) == "int":
        str(nb)
    s = 0
    for i in range(len(nb)):
        s = s + int(nb[-i-1]) * b**i
    return s




def dec_vers_base_b(nb, b):
    nb_base_b = ""
    if nb == 0:
        return 0
    while nb > 0:
        nb_base_b = str(nb % b) + nb_base_b
        nb = nb // b
    return int(nb_base_b)

def base_b1_vers_base_b2(b1,b2,nb):
    return dec_vers_base_b(base_b_vers_dec(nb, b2), b2)

def dec_vers_hex(nb):
    return dec_vers_base_b(nb,16)
    

def est_representable_bin(nb, b):
    if b <= 0:
        return False
    return 0 <= nb < 2**b


def est_representable_comp2(nb, b):
    if b <= 0:
        return False
    return -2**(b-1) <= nb < 2**(b-1)
    

def addition_binaire_machine(nb1, nb2, b):
    somme = []
    retenue = 0
    nb1 = [0]*(b-len(nb1)) + nb1
    nb2 = [0]*(b-len(nb2)) + nb2
    for i in range(b-1,-1,-1):
        if nb1[i]+nb2[i]+retenue >= 2:
            somme.append(nb1[i]+nb2[i]+retenue-2)
            retenue = 1
        else:
            somme.append(nb1[i]+nb2[i]+retenue)
            retenue = 0
    somme.append(retenue)
    return somme[::-1]
    
def bin_vers_dec(nb):
    return base_b_vers_dec(nb, 2)
        
def comp2_vers_dec(b, nb):
    nb = [0]*(b-len(nb)) + nb[-b:]
    signe = 1
    if nb[0] == 1:
        for i in range(b):
            nb[i] = nb[i]*-1+1
        nb = addition_binaire_machine(nb, [1], b)
        signe = -1
    return bin_vers_dec(nb) * signe

def test_fonction_17_a_26():
    
    
    #Test fonction 20:
    
    incorrecte = False
    for i in range(100):
        for j in range(100):
            if addition_binaire_machine([int(elm) for elm in str(dec_vers_base_b(j, 2))],[int(elm) for elm in str(dec_vers_base_b(i, 2))], 15)!= [0]*(16-len([int(elm) for elm in str(dec_vers_base_b(i+j, 2))]))+[int(elm) for elm in str(dec_vers_base_b(i+j, 2))]:
                incorrecte = True
                print("Erreur pour addition_binaire_machine(",i,",",j,", 15 ): donne ",addition_binaire_machine([int(elm) for elm in str(dec_vers_base_b(j, 2))],[int(elm) for elm in str(dec_vers_base_b(i, 2))], 15), "au lieu de :",[0]*(16-len([int(elm) for elm in str(dec_vers_base_b(i+j, 2))]))+[int(elm) for elm in str(dec_vers_base_b(i+j, 2))])
    if not(incorrecte):
        print("Fonction addition_binaire_machine() correcte")
    #Ici  on regarde si bin(i)+bin(j) == bin(i+j) pour toute combinaison de nombres i,j appartenant à [0,100]
    #Si ce n'est pas le cas, la fonction addition binaire n'est pas fonctionnel
    #On considaire la fonction dec_vers_base_b() fonctionnel
    
    
    #Test fonction 21:
    
test_fonction_17_a_26()
