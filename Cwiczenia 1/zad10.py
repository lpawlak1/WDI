# Zadanie 10. Napisać program wyszukujący liczby doskonałe mniejsze od miliona.
def cw10():
    maximum = 10**6
    for a in range(4, maximum+1):
        suma = 0
        for i in range(a-1, 0, -1):
            if a % i == 0:
                suma += i
        if suma == a:
            print(a, "Jest dobra")
