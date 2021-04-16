# Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
# parzystą.

def cw03(MAX, t):
    for i in range(MAX):
        for j in range(MAX):
            copy = t[i][j]
            while copy > 0:
                if (copy % 10) % 2 == 0:
                    break
                copy //= 10
            else:
                break
        else:
            return True
    return False
