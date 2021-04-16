null = None


class lista:
    def __init__(self, first=null):
        self.first = first

    def __str__(self):
        cp = self.first
        if cp == null:
            return "List is empty!"
        ret = ""
        while cp is not None:
            ret = ret + str(cp)
            cp = cp.next
        return ret

    def is_empty(self):
        return self.first == null


class Node:
    # val,next,idx
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return f"{self.val}-->"


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e, ret.first)
    return ret


# 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
# funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
# powstać nowa lista.
def usun_nadliczby(first):
    if first.next == null:
        if first.val < 10:
            return first
        a = Node(first.val // 10, first)
        first.val %= 10
        return a
    cp = first
    cp2 = first.next
    while cp2.next != null:
        cp, cp2 = cp2, cp2.next
    cp.next = null
    cp.val += cp.val // 10
    ret = usun_nadliczby(first)
    cp2.val = cp2.val % 10
    cp.next = cp2
    return ret


def add_two(f1, f2):
    def rek(first, second):
        if first.next == null and second.next == null:
            buffer = (first.val + second.val) // 10
            return Node((first.val + second.val) % 10), buffer
        if first.next == null:
            nowy, buffer = rek(first, second.next)
            buffer = (second.val + buffer)
            return Node(buffer % 10, nowy), buffer // 10
        if second.next == null:
            nowy, buffer = rek(first.next, second)
            buffer = (first.val + buffer)
            return Node(buffer % 10, nowy), buffer // 10

        stary, buffer = rek(first.next, second.next)
        buffer = (first.val + second.val + buffer) // 10
        nowy = Node((buffer + first.val + second.val) % 10, stary)
        return nowy, buffer

    a, b = rek(f1, f2)
    if b > 0:
        return Node(1, a)
    return a


f1 = tabToLista([1, 2, 3])
f2 = tabToLista([2, 2])
print(f1)
print(f2)
print(lista(add_two(f1.first, f2.first)))
