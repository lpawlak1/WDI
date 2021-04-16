# Zadanie 27. Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę
# napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących
# na siebie kwadratów, których suma pól jest równa 2012 i False w
# przeciwnym przypadku.

# x1,x2,y1,y2
def check(t):
    suma = 0
    for i in range(13):
        # suma
        suma += abs((t[i][0] - t[i][1]) * (t[i][2]-t[i][3]))
        for j in range(i+1, 13):
            # czy nachodza
            if t[j][0] > t[i][0] and t[j][0] < t[i][1] and (
                (t[j][2] > t[i][2] and t[j][2] < t[i][3])
                    or (t[j][3] > t[i][2] and t[j][3] < t[i][3])):
                return False
            elif t[j][1] > t[i][0] and t[j][1] < t[i][1] and ((t[j][2] > t[i][2] and t[j][2] < t[i][3]) or (t[j][3] > t[i][2] and t[j][3] < t[i][3])):
                return False
    if suma == 2012:
        return True
    return False


def reku(tab, pomc, index, idx_pom):
    if idx_pom == 13:
        return check(pomc)
    if index == len(tab):
        return False
    a = reku(tab, pomc, index+1, idx_pom)
    pomc[idx_pom] = tab[index]
    idx_pom += 1
    b = reku(tab, pomc, index+1, idx_pom)
    return a or b


def fun(tab):
    return reku(tab, [0 for _ in range(13)], 0, 0)
