from cw01 import odejmowanie, dzielenie

# Zadanie 4. Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
# zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.


def cw4(tab: list):
    lg_max = 0
    la_max = 0
    la_curr, r = 2, odejmowanie(tab[1], tab[0])
    lg_curr, q = 2, dzielenie(tab[1], tab[0])
    i = 2
    while i < len(tab):
        od = odejmowanie(tab[i], tab[i-1])
        if od[0] == r[0] and od[1] == r[1]:
            la_curr += 1
        else:
            if la_curr > 2:
                la_max += 1
            la_curr = 2
            r = od
        q1 = dzielenie(tab[i], tab[i-1])
        if q1[0] == q[0] and q1[1] == q[1]:
            lg_curr += 1
        else:
            if lg_curr > 2:
                lg_max += 1
            lg_curr = 2
            q = q1
        i += 1
    if lg_max > la_max:
        return 1
    elif la_max > lg_max:
        return 0
    return -1


t = [(1, 2) for _ in range(100)]
print(cw4(t))
