# Zadanie 17. Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
# ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości
# początkowych wyrazów ciągu.
def cw17(a=1, b=1):
    a1, a2 = a, b
    iloraz_1, iloraz_2 = 1.0, 10101010101010101010.0
    while abs(iloraz_1 - iloraz_2) > 0.00000000001:
        a1, a2 = a2, a1+a2
        iloraz_1, iloraz_2 = iloraz_2, a2/a1
    return iloraz_2
