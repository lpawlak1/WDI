# Zadanie 11. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# jej cyfry stanowią ciąg rosnący.

def cw11():
    num = int(input(">: "))

    a = num % 10
    num //= 10
    while num != 0:
        temp = num % 10
        num = num // 10
        if temp > a:
            return False
        a = temp
    return True


if __name__ == "__main__":
    print(cw11())
