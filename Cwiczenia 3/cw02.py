# Zadanie 2. Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy są one
# zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

def cw2():
    a = int(input("podaj 1 liczbe:"))
    b = int(input("podaj 2 licbze: "))

    a_t = [-1 for _ in range(10)]
    i = 0
    while a > 0:
        a_t[i] = (a % 10)
        a //= 10
        i += 1

    while b > 0:
        temp = b % 10
        b //= 10
        i = 0
        while i < len(a_t):
            if temp == a_t[i]:
                a_t[i] = -1
                break
            i += 1
        else:
            return False

    for e in a_t:
        if e != -1:
            return False
    return True
