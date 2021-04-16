# Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba naturalna jest palindromem, a następnie czy jest palindromem w
# systemie dwójkowym.
def czy_jest_palindrom():
    liczba = int(input("Podaj liczbe..."))
    lsum = liczba
    rsum = 0
    while liczba > 0:
        rsum = (rsum*10) + liczba//10
        liczba //= 10

    if not rsum == lsum:
        return False

    liczba = lsum
    rsum = 0
    while liczba > 0:
        rsum = (rsum*2) + (liczba % 2)
        liczba //= 2

    return lsum == rsum


if __name__ == "__main__":
    print(czy_jest_palindrom())
