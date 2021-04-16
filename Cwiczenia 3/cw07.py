from random import randint
# Zadanie 7. Napisać program wypełniający N-elementową tablicę t liczbami
# naturalnymi 1-1000 i sprawdzający czy istnieje element tablicy zawierający
# wyłącznie cyfry niepar


def cw7():
    MAX = 150
    tab = [randint(0, 1000) for _ in range(MAX)]
    i = 0
    while i < len(tab):
        copy = tab[i]
        while copy > 0:
            if copy % 2 == 0:
                break
            copy //= 10
        else:
            return True
        i += 1
    return False
