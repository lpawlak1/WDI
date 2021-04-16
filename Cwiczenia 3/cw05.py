# Zadanie 5. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem
# stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
# wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się
# wystarczająca liczba elementów.

prompt = "10 wartosc co do wartosci, zakoncz zerem"
temp = int(input(prompt))
t = [0 for _ in range(100)]
k = 0
while temp != 0:
    t[k] = temp
    temp = int(input(prompt))
    k += 1
# end while

t_10 = [0 for _ in range(10)]
i = 0
while i < k:
    if t[i] > t_10[9]:
        for j in range(k):
            if t[i] > t_10[j]:
                # alter all and insert in
                m = j
                temp = t_10[m]
                t_10[m] = t[i]
                while m < 10-1:
                    temp, t_10[m+1] = t_10[m+1], temp
                    m += 1
                break
    i += 1
print(t_10[9])
