from math import pi
# Zadanie 14. Napisać program obliczający wartości cos(x) z rozwinięcia w
# szereg Maclaurina.


def szereg(x, n):
    return ((-1)**n)*(x**(2*n))/silnia(2*n)


def silnia(nr):
    ret = 1
    for i in range(2, nr+1):
        ret *= i
    return ret


def cw14():
    x = 2*pi
    x_1 = 0
    x_2 = 12
    n = 0
    suma = 0
    while abs(x_1 - x_2) > 0.0000001:
        x_1, x_2 = x_2, szereg(x, n)
        suma += x_2
        print(suma)
        n += 1
