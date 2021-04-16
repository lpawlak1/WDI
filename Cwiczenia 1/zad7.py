# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu
# Fibonacciego.
def cw7():
    liczba_szukana = int(input("Podaj liczbe:"))
    a1 = 1
    a2 = 1
    while a1*a2 < liczba_szukana:
        new_number = a2+a1
        a1 = a2
        a2 = new_number
    if a1*a2 == liczba_szukana:
        return True
    return False
