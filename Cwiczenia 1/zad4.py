# Zadanie 4. Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n
# 2
def cw4(searched_number):
    suma = 0
    ret = 1
    while True:
        suma += (2*ret - 1)
        if suma == searched_number:
            return ret
        if suma > searched_number:
            return ret-1
        ret += 1
