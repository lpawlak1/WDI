# Zadanie 13. Napisać program wyznaczający najmniejszą wspólną
# wielokrotność 3 zadanych liczb.
def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def cw13():
    # nww = a*b*c / nwd
    a = 14
    b = 3
    c = 6
    nww_a_b = a*b//nwd(a, b)
    nww_a_c = a*c//nwd(a, c)
    nww_b_c = b*c//nwd(b, c)
    return max(nww_a_b, nww_a_c, nww_b_c)
