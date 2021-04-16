# Zadanie 19. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego podciągu
# rosnącego dla którego suma jego elementów jest równa sumie indeksów tych
# elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić
# długość znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
from random import randint


def cw19(N, t):
    m = 0

    i = 0
    while i < N-1:
        j = i+1
        suma = 0
        suma_index = 0
        temp = t[i]
        count = 0
        while j < N:
            if t[j] > temp:
                suma += t[j]
                suma_index += j
                temp = t[j]
                if suma == suma_index:
                    count += 1
                    if count > m:
                        m = count
                j += 1
            else:
                break
        i += 1
    return m


if __name__ == "__main__":
    print(cw19(50, [randint(1, 5) for _ in range(50)]))
