# Zadanie 16. Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę
# napisać funkcję zwracającą wartość typu bool oznaczającą, czy w tablicy
# istnieje dokładnie jeden element najmniejszy i dokładnie
# jeden element największy (liczba elementów najmniejszych oznacza liczbę
# takich elementów o tej samej wartości)
def czy_jes_naj(t):
    mmin = t[0]
    count_min = 1
    mmax = t[0]
    count_max = 1
    i = 1
    while i < len(t):
        if t[i] < mmin:
            mmin = t[i]
            count_min = 1
        elif t[i] == mmin:
            count_min += 1

        if t[i] > mmax:
            mmax = t[i]
            count_max = 1
        elif t[i] == mmax:
            count_max += 1
        i += 1

    return count_max == 1 and count_min == 1
