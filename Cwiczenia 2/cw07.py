# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

def wielokrotnosc():
    szukana = int(input(">:"))

    n = 1
    wyraz_ciagu = (n*n)+n+1

    while wyraz_ciagu < szukana:
        if szukana % wyraz_ciagu == 0:
            return True
        n += 1
        wyraz_ciagu = (n*n)+n+1
    if wyraz_ciagu == szukana:
        return True
    return False


if __name__ == "__main__":
    print(wielokrotnosc())
