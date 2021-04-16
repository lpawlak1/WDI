# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym
# możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)
def czy_zlozona(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return False
    if num % 2 == 0 or num % 3 == 0:
        return True
    i = 6
    if (i-1)**2 <= num:
        if num % (i-1) == 0 or num % (i+1) == 0:
            return True
        i += 6
    return False


def bin_to_dec(s):
    num = 0
    waga = len(s)-1
    for i in range(len(s)):
        num += int(s[i])*(10**(waga))
        waga -= 1
    return num


def is_it(s):
    if czy_zlozona(bin_to_dec(s)):
        print(s)


def rec(s, a_rem, b_rem):
    if a_rem == 0 and b_rem == 0:
        is_it(s)
        return
    if a_rem > 0:
        rec(s + "1", a_rem-1, b_rem)
    if b_rem > 0:
        rec(s + "0", a_rem, b_rem-1)


def func(a, b):
    if a <= 0 or b <= 0:
        return ""
    rec("1", a-1, b)


func(3, 2)
