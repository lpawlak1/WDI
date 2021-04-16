# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.
null = None


class Node:
    def __init__(self, value=null, next=null):
        self.val = value
        self.next = next

    def __str__(self):
        return f"{self.val}-->"


def wypisz(first):
    if first == null:
        print("List is empty!")
    while first != null:
        print(first, end='')
        first = first.next
    print()


class Node2:
    # val,next,idx
    def __init__(self, val=0, next=None, idx=0):
        self.next = next
        self.val = val
        self.idx = idx

    def __str__(self):
        return f"{self.idx},{self.val}"


def init(num):
    return Node2(num)


def insertIfNotInList(first, key):
    if first.next == null:
        first.next = Node2(val=key, idx=1)
        return False
    cp = first.next
    while cp.next != null:
        if key == cp.val:
            if cp.idx >= 2:
                return True
            cp.idx += 1
            return False
        cp = cp.next
    if key == cp.val:
        if cp.idx >= 2:
            return True
        cp.idx += 1
        return False
    cp.next = Node2(key, idx=1)
    return False


def delete(cp, cp2):
    cp.next = cp2.next
    del cp2


def check(first, rzadka_tablicka=init(0), last=False):
    if first == null:
        return null
    if first.next == null:
        return first
    insertIfNotInList(rzadka_tablicka, first)
    cp, cp2 = first, first.next
    while cp2 != null:
        if insertIfNotInList(rzadka_tablicka, cp2.val):
            delete(cp, cp2)
            cp, cp2 = cp, cp.next
            continue
        cp, cp2 = cp2, cp2.next
    if last == False:
        return check(first, rzadka_tablicka, True)
    return first


def check2(first):
    if first is None:
        return None
    if first.next is None:
        return first
    head = Node("!", first)
    cp, cp2 = head, first
    while cp2 is not None:
        a = cp2
        flag = True
        while a.next != null:
            if a.next.val == cp2.val:
                a.next = a.next.next
                flag = False
            else:
                a = a.next
        if not flag:
            cp.next = cp2.next
            cp2 = cp.next
        else:
            cp, cp2 = cp.next, cp2.next
    return head.next


first = Node(1)
for i in range(1, 10):
    a = Node(9, first)
    first = a
wypisz(first)
wypisz(check2(first))
