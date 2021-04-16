# Zadanie 14. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
def cw14(num1, num2):
    count = 0
    count += rekurencja(num1, num2, 1, "")
    count += rekurencja(num1, num2, 2, "")
    return count


def rekurencja(num1, num2, index, new: str):
    count = 0
    new = new + str(num1 % 10) if index == 1 else str(num2 % 10)
    if index == 1:
        num1 //= 10
    else:
        num2 //= 10
    if num1 != 0:
        count += rekurencja(num1, num2, 1, new)
    if num2 != 0:
        count += rekurencja(num1, num2, 2, new)
    if num1 == 0 and num2 == 0:
        final_num = int(new)
        i = 3
        if final_num % 2 == 0:
            return count
        while i*i < final_num:
            if final_num % i == 0:
                return count
            i += 2
        return count + 1
    return count


if __name__ == "__main__":
    print(cw14(12345, 876543))
