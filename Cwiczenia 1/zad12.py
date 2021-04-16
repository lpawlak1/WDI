# Zadanie 12. Napisać program wyznaczający największy wspólny dzielnik 3
# zadanych liczb.
def cw12(a=60, b=30, c=105):
    return min(nwd(a, b), nwd(a, c), nwd(b, c))


def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a
