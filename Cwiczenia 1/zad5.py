# Zadanie 5. Proszę napisać program wyznaczający pierwiastek kwadratowy ze
# wzoru Newtona.
def cw5(liczba=25):
    n = 2
    a = 1
    b = 123
    e = 0.00000000001
    while abs(b-a) >= e:
        b, a = (1/n)*((n-1)*a+(liczba/(a**(n-1)))), b
    return a, b
