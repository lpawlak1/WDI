# Zadanie 13. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba zakończona jest unikalną cyfrą.
def cw13():
    liczba = int(input("Podaj liczbe.."))
    last = 0
    last = liczba % 10
    liczba //= 10
    while liczba != 0:
        if last == liczba % 10:
            return False
        liczba //= 10
    return True


if __name__ == "__main__":
    print(cw13())
