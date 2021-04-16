# Zadanie 14. Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
# np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2¿N1. Proszę napisać funkcję,
# która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
# elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
# pozostać nie zmieniane.
def czy_pierwsza(num):
    # to tylko cyfry pierwsze nie liczby
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    return False


def funcn(t, MAX):
    for row in t:
        i = 0
        jest = False
        while i < MAX:
            copy = row[i]
            j = False
            while copy > 0:
                if czy_pierwsza(copy % 10):
                    j = True
                copy //= 10
            if not j:
                break
            i += 1
        else:
            return True
    return False


if __name__ == "__main__":
    print(
        funcn(
            [[23, 26, 35, 71],
             [21, 123, 45, 8],
             [4, 4, 4, 4],
             [6, 6, 8, 3]],
            4))
