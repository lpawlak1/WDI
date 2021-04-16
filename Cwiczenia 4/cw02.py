# Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę
# napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.

def cw02(MAX, t):
    # row
    for i in range(MAX):
        is_there = False
        # column
        for j in range(MAX):
            si = True
            copy = t[i][j]
            while copy > 0:
                if (copy % 10) % 2 == 0:
                    si = False
                    break
                copy //= 10
            if si:
                is_there = True
                break
        if not is_there:
            return False
    return True
