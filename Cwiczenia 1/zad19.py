# Zadanie 19. Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! +
# 1/2! + 1/3! + ...
def cw19():
    ret = 1.0
    curr_silnia = 1
    for i in range(1, 1000+1):
        curr_silnia = curr_silnia * i
        ret += 1/(curr_silnia)
    return ret
