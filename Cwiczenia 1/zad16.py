# Zadanie 16. Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
# początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po
# największej liczbie kroków.
def cw16():
    maxymalna_wartosc: int = 0
    liczba = 0
    for i in range(2, 10000+1):
        count = 0
        a_n = i
        while abs(a_n - 1.0) > 0.000000054:
            a_n = cw16_rek(a_n)
            count += 1
        if count > maxymalna_wartosc:
            maxymalna_wartosc = count
            liczba = i
    return maxymalna_wartosc, liczba


def cw16_rek(a_n):
    return (a_n % 2)*(3*a_n + 1) + (1-a_n % 2) * (a_n/2)
