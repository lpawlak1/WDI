# Zadanie 18. Zmodyfikować wzór Newtona aby program z zadania 5 obliczał
# pierwiastek stopnia 3.
def cw18(A=125.0):
    n = 3
    a = 1
    b = 123
    e = 0.00000000001
    while abs(b-a) >= e:
        b, a = (1/n)*((n-1)*a+(A/(a**(n-1)))), b
    return a, b
