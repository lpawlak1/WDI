# Zadanie 6. Napisać program wypełniający N-elementową tablicę t liczbami
# naturalnymi 1-1000 i sprawdzający czy każdy element tablicy zawiera co
# najmniej jedną cyfrę nieparzystą.
def cw06(tab):
    i = 0
    while i < len(tab):
        copy = tab[i]
        while copy > 0:
            if (copy % 10) % 2 == 1:
                break
            copy //= 10
        else:
            return False
        i += 1
    return True
