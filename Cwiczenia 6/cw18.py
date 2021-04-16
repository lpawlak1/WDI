# Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę
# naturalną. Na ruchy króla
# Nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# Polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# W=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# Narożnika
def can_move(tab, from_col, from_row, to_col, to_row, gdzie_byl):
    to_ = 0
    from_ = 0
    if to_col >= 0 and to_col <= 7 and to_row >= 0 and to_row <= 7:
        to_ = tab[to_row][to_col]
        from_ = tab[from_row][from_col]
        if gdzie_byl[to_row][to_col] == 1:
            return False
    else:
        return False
    if from_ % 10 < int(str(to_)[0]) and max(
            abs(7-from_col), abs(7-from_row)) >= max(abs(7-to_col), abs(7-to_row)):
        return True
    return False


def rekur(row, column, tab, gdzie_byl: list):
    gdzie_byl[row][column] = 1
    if row == 7 and column == 7:
        return True
    ruchy = ((1, 1), (1, 0), (0, 1), (1, -1))
    for elem in ruchy:
        if can_move(tab, column, row, column+elem[1], row+elem[0], gdzie_byl):
            if rekur(row+elem[0], column+elem[1], tab, gdzie_byl):
                return True
        if can_move(tab, column, row, column-elem[1], row-elem[0], gdzie_byl):
            if rekur(row-elem[0], column-elem[1], tab, gdzie_byl):
                return True
    gdzie_byl[row][column] = 0
    return False


def func(tab):
    empty = [[0 for _ in range(8)] for _ in range(8)]
    a = rekur(0, 0, tab, empty)
    return a


tab = [
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 82, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 91, 2],
    [1, 4, 6, 82, 3, 5, 24, 2],
    [1, 4, 6, 2, 3, 5, 35, 7],
    [1, 4, 6, 2, 3, 5, 35, 8],
]
print(func(tab))
