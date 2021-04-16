# Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2  ] rozwiązaniem jest liczba 10.

def rekur(tab, index, suma, suma_ind, pusty: bool):
    if index == len(tab):
        if pusty:
            if suma == suma_ind:
                return suma
        return False
    a = rekur(tab, index+1, suma, suma_ind, pusty)
    if a != False:
        return a
    suma += tab[index]
    suma_ind += index
    pusty = True
    a = rekur(tab, index+1, suma, suma_ind, pusty)
    if a != False:
        return a
    return False


def func(tab):
    return rekur(tab, 0, 0, 0, False)


print(func([1, 7, 3, 5, 11, 2]))
