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


