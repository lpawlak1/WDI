# Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną
# i zwraca sumę iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
# że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej.
# Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71
def na_czynniki_p(num):
    i = 2
    t = []
    while num != 1:
        if num % i == 0:
            t.append(i)
            while num % i == 0:
                num //= i
        i += 1
    return t


def reku(tab, idx, num):
    if len(tab) == idx:
        if num != 1:
            return num
        return 0
    suma = 0
    suma += reku(tab, idx+1, num)
    num *= tab[idx]
    suma += reku(tab, idx+1, num)
    return suma


def func(num):
    return reku(na_czynniki_p(num), 0, 1)


print(func(1234))
