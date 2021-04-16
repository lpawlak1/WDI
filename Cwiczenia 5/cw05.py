# Zadanie 5. Dany jest zbiór punktów leżących na płaszczyźnie opisany przy
# pomocy struktury dane =
# [(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
# tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
# punktów.
def cw05(dane):
    for i in dane:
        for e in dane:
            # tylko w prawo
            if i[1] == e[1] and i[0] < e[0]:
                dlugosc = e[0]-i[0]
                # tylko w gore
                poziomA = i[1] + dlugosc
                countA = 0
                b = False
                for f in dane:
                    if (f[0] > i[0] and f[0] < e[0]) and (
                            f[1] > i[1] and f[1] < poziomA):
                        break
                    elif f[1] == poziomA:
                        if f[0] == i[0] or f[0] == e[0]:
                            countA += 1
                            if countA == 2:
                                b = True
                else:
                    if b:
                        return True
    return False


if __name__ == "__main__":
    print(cw05([(1, 1), (1, 4), (4, 1), (4, 4), (1, 2)]))
