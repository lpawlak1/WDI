# Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję,
# która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.
def can_take(tab, index, tablica):
    if tablica[index] == False:
        return True
    return False


def reku(tab, suma_curr, suma_zad, index, tablica):
    if suma_curr == suma_zad:
        return True
    elif suma_curr > suma_zad:
        return False
    elif index == (len(tab)**2) - 1:
        return False
    if reku(tab, suma_curr, suma_zad, index+1, tablica):
        return True
    if can_take(tab, index, tablica):
        tablica[index] = True
        if reku(
                tab, suma_curr + tab[index // len(tab)][index % len(tab)],
                suma_zad, (index // len(tab)) + 1, tablica):
            return True
        tablica[index] = False
    return False


def func(tab, suma):
    tablica = [False for _ in range(len(tab)**2)]
    return reku(tab, 0, suma, 0, tablica)


tab = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]

print(func(tab, 4))
