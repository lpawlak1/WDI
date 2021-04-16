# Zadanie 4. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
# 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
# od 1 do N włącznie.
# 2-3-5
def counter(N: int):
    count = 0
    while N >= 1:
        a = N
        while a % 2 == 0:
            a //= 2
        while a % 3 == 0:
            a //= 3
        while a % 5 == 0:
            a //= 5
        if a == 1:
            count += 1
        N -= 1
    return count


if __name__ == "__main__":
    print(counter(1_000_000))
