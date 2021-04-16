from math import pi, sqrt
# Zadanie 11. Napisać program wyszukujący liczby zaprzyjaźnione mniejsze
# od miliona.


def cw11():
    maximum = 10**4
    for a in range(2, maximum+1):
        suma_a = 1
        for i in range(int(sqrt(a)), 1, -1):
            if a % i == 0:
                suma_a += (a//i) + i
        suma_b = 1
        for i in range(int(sqrt(suma_a)), 1, -1):
            if suma_a % i == 0:
                suma_b += (suma_a//i) + i
        if suma_b == a and suma_a < a:
            print(a, suma_a, "Są dobre ...")
