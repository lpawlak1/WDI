# Zadanie 3. Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
# hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać
# położenie hetmanów.
def szachuj_(danee):
    i = 0
    while i < len(danee):
        j = i+1
        while j < len(danee):
            # wiersz
            if danee[j][0] == danee[i][0]:
                return False
            # kolumna
            if danee[j][1] == danee[i][1]:
                return False
            # na skos
            x = abs(danee[i][0] - danee[j][0])
            y = abs(danee[i][1] - danee[j][1])
            if x // y == 1:
                return False
            j += 1
        i += 1
    return True
    # ? false to sie szachuja a true to sie nie szachuja


dane = [(i, i % 10) for i in range(100)]
dane = [(1, 4), (0, 5)]
print(szachuj_(dane))
