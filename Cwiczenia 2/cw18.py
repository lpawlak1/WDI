# Zadanie 18. Mamy dane dwa ciągi A,B o następujących zależnościach:
#     A: a0 = 0, a1 = 1, an = an−1 − bn−1 ∗ an−2
#     B: b0 = 2, bn = bn−1 + 2 ∗ an−1
#     Proszę napisać program, który czyta liczby typu int ze standardowego wejścia i tak długo jak liczby te są
#     kolejnymi wyrazami ciągu An (tj. a0, a1, a2, ...) wypisuje na standardowe wyjście wyrazy drugiego ciągu Bn
#     (tj. b0, b1, b2, ...).
def cw18():
    a0, a1 = 0, 1
    b0 = 2
    a2 = a1 - (b0 * a0)
    b1 = b0 + (2 * a1)
    while int(input(">")) == a0:
        print(b0)
        a0, a1, b0, a2, b1 = a1, a2, b1, a1 - (b0 * a0), b0 + (2 * a1)


if __name__ == "__main__":
    cw18()
