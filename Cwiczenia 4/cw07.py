# Zadanie 7. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
# T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
# T2 były uporządkowane niemalejąco.

def cw07(MAX):
    t1 = [[i+(MAX*j) for i in range(MAX)] for j in range(MAX)]
    t2 = [-1 for _ in range(MAX*MAX)]

    i = 0
    while i < MAX:
        j = 0
        while j < MAX:
            index = 0
            temp = t1[i][j]
            while index < MAX*MAX:
                if temp >= t2[index]:
                    while index < MAX*MAX:
                        t2[index], temp = temp, t2[index]
                        if t2[index] == -1:
                            break
                        index += 1
                    break
                index += 1
            j += 1
        i += 1
    return t2


if __name__ == "__main__":
    print(cw07(10))
