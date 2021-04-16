# Zadanie 12. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta zawiera cyfrę równą liczbie swoich cyfr.
def cw12():
    liczba = int(input("> :"))
    lenght = 0

    num = liczba
    while num != 0:
        lenght += 1
        num //= 10

    num = liczba
    while num != 0:
        temp = num % 10
        if temp == lenght:
            return True
        num //= 10
    return False


if __name__ == "__main__":
    print(cw12())
