# Zadanie 1. Proszę napisać program wypisujący elementy ciągu Fibonacciego
# mniejsze od miliona.
def cw1():
    a1 = 1
    a2 = 1
    while a1 < 10**6:
        print(a1)
        a1, a2 = a2, a1+a2
