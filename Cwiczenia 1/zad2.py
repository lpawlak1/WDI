# Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

def cw2(target):
    best = target
    result_a = 0
    result_b = 0
    for a in range(1, target//2):
        for b in range(1, target//2):
            f0 = a
            f1 = b
            while(f0 + f1 <= target):
                new_number = f0 + f1
                if new_number == target and a+b < best:
                    result_a = a
                    result_b = b
                    best = a+b
                f0, f1 = f1, new_number
    return (f"ta pierwsza to {result_a} a ta druga to {result_b}")
