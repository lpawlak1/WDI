# Zadanie 20. Dane są ciągi: An+1 =
# √
# An ∗ Bn oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne do
# wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. Napisać program wyznaczający średnią
# arytmetyczno-geometryczną dwóch liczb.
def cw20():
    a_n = 20.0
    b_n = 30.0
    a_n, b_n = (a_n*b_n)**(0.5), (a_n+b_n)/2.0
    while abs(a_n - b_n) > 0.000000000001:
        a_n, b_n = (a_n*b_n)**(0.5), (a_n+b_n)/2.0
    return b_n
