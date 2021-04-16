from random import randint
# Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę
# napisać funkcję, która w
# poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
# co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
# się znaleźć taki ciąg oraz długość tego ciągu.


def cw08(t1, MAX):
    c_amx = 0
    i = 0
    while i <= MAX-3:
        count = 0
        copy = i+1
        row = 1
        a1 = t1[0][i]
        q = 12
        while copy < MAX:
            if q == 0:
                break
            if a1 * q == t1[row][copy]:
                a1 = a1*q
                count += 1
            else:
                if a1 == 0:
                    break
                q = t1[row][copy] / a1
                count = 2
            row += 1
            copy += 1
        if count > c_amx:
            c_amx = count
        i += 1

    if c_amx >= 3:
        return True, c_amx
    return False


if __name__ == "__main__":
    print(cw08([[randint(1, 100) for _ in range(100)]
                for _ in range(100)], 100))
