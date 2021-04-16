# Zadanie 1. Napisać funkcję zamieniającą i wypisującą liczbę naturalną na
# system o podstawie 2-16.
a = int(input("podaj liczbe: "))
podstawa = int(input("podaj podstawe: "))
new_a = ""
while a > 0:
    temp = a % podstawa
    if temp >= 10:
        temp = chr(temp+55)
    new_a = str(temp) + new_a
    a //= podstawa
print(new_a)
