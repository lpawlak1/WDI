# Zadanie 8. Napisać program sprawdzający czy zadana liczba jest pierwsza.
def cw8(liczba):
    if liczba % 2 == 0:
        return "tak"
    n = 3
    while n < (liczba*(0.5))+1:
        if liczba % n == 0:
            return "tak"
        n += 1
    return "nie"
