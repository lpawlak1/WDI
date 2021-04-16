# Zadanie 9. Napisać program wypisujący podzielniki liczby.
def cw9(liczba):
    for i in range(liczba//2, 0, -1):
        if liczba % i == 0:
            print(i)
