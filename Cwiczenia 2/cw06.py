# Zadanie 6. Napisać program wczytujący liczbę naturalną z klawiatury i
# rozkładający ją na iloczyn 2 liczb
# o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.
if __name__ == "__main__":
    num = int(input(">: "))
    i = 3
    a = num
    b = 1
    min_roznica = num

    if num % 2 == 0 and abs(2 - (num//2)) < min_roznica:
        a = 2
        b = num//2
        min_roznica = abs(2 - (num//2))

    while i < num:
        if num % i == 0 and abs(i - (num//i)) < min_roznica:
            a = i
            b = num//i
            min_roznica = abs(i - (num//i))
        i += 1
    print(a, b)
