# Zadanie 30. Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
# współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać funkcję, która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n¡k oraz n jest wielokrotnością liczby
# 3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
# należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
# wartość typu bool.
from math import sqrt


def check(tab, r, k, idx):
    if idx % 3 != 0 or idx == 0:
        return False
    if idx >= k:
        return False
    x = 0
    y = 0
    i = 0
    while i < idx:
        x += tab[i][0]
        y += tab[i][1]
        i += 1
    x /= i
    y /= i
    dl = sqrt((x**2) + (y**2))
    if dl <= r:
        return True
    return False

# (x,y)


def reku(tab, pomc, idx, r, k, pom_idx):
    if len(tab) == idx:
        return check(pomc, r, k, pom_idx)
    if reku(tab, pomc, idx+1, r, k, pom_idx):
        return True
    pomc[pom_idx] = tab[idx]
    if reku(tab, pomc, idx+1, r, k, pom_idx+1):
        return True
    return False


def func(tab, r, k):
    return reku(tab, [0 for _ in range(len(tab))], 0, r, k, 0)
