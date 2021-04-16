# Zadanie 20. Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry.
# Proszę napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
# taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
# podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11)
def cw20(a, b):
    i = 2
    while i <= 16:
        print(i)
        a1, a2 = "", ""
        cpa, cpb = a, b
        #a1, a
        while cpa >= 1:
            temp = getLiczba(cpa % i)
            print(temp, end=" ")
            if not temp in a1:
                a1 = a1 + temp
            cpa //= i
        # end while

        ishere = False
        #a2, b
        while cpb >= 1:
            temp = getLiczba(cpb % i)
            if temp in a1:
                print("2", end=" ")
                ishere = True
                break
            cpb //= i
        # end while

        if not ishere:
            return("jest taka ze " + str(i))
        i += 1
    # end while
    return "falsea"
# end def


def getLiczba(num):
    if num < 10:
        return str(num)
    elif num == 10:
        return "A"
    elif num == 11:
        return "B"
    elif num == 12:
        return "C"
    elif num == 13:
        return "D"
    elif num == 14:
        return "E"
    elif num == 15:
        return "F"


if __name__ == "__main__":
    print(cw20(a=123, b=522))
