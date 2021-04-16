# 20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
# Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
# napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
# Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
# powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]
null = None


class Node:
    class przedzial:
        def __init__(self, a=0, b=0):
            self.a = a
            self.b = b

        def wsp_pr(self, pr):
            return min(pr.a, self.a), max(pr.b, self.b)

        def zawiera(self, pr):
            return pr.a <= self.a <= pr.b or \
                   pr.a <= self.b <= pr.b

        def __str__(self):
            return f"[{self.a},{self.b}]"

    def __init__(self, val=null, next=null):
        self.val = val
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


def check(first):
    if first == null:
        return null
    if first.next == null:
        return first
    buf = first
    flag = False
    cp = first.next
    while cp != null and first.val.zawiera(cp.val):
        a = first.val.wsp_pr(cp.val)
        first.val = Node.przedzial(a[0], a[1])
        flag = True
        first.next = cp.next
        cp = cp.next
    if first.next == null:
        cp2 = null
    else:
        cp2 = first.next.next
    cp = first.next
    while cp2 != null:
        if first.val.zawiera(cp2.val):
            a = first.val.wsp_pr(cp2.val)
            first.val = Node.przedzial(a[0], a[1])
            flag = True
            cp.next = cp2.next
            del cp2
            cp2 = cp.next
            continue
        cp, cp2 = cp2, cp2.next
    first = first.next
    cp.next = buf
    buf.next = null
    if flag:
        if first.next.next == null:
            if first.val.zawiera(first.next.val):
                a = first.val.wsp_pr(cp2.val)
                first.val = Node.przedzial(a[0], a[1])
                first.next = null
                return first
        return check(first)
    return first


first = Node(Node.przedzial(15, 19), Node(Node.przedzial(2, 5), Node(Node.przedzial(7, 11), Node(Node.przedzial(8, 12),
                                                                                                 Node(Node.przedzial(5,
                                                                                                                     6),
                                                                                                      Node(
                                                                                                          Node.przedzial(
                                                                                                              13, 17),
                                                                                                          Node(Node.przedzial(5,8),
                                                                                                               Node(Node.przedzial(11,14)))))))))

wypisz(first)
wypisz(check(first))


def pushBack(first, l, r):
    p = first
    prev = None
    while p != None:
        p, prev = p.next, p
    prev.next = Node(Node.przedzial(l, r))
    return first


z = Node(Node.przedzial(-5,-3))
z = pushBack(z, 15, 19)
z = pushBack(z, 2, 5)
z = pushBack(z, 7, 11)
z = pushBack(z, 6, 7)
z = pushBack(z, 8, 12)
z = pushBack(z, 5, 6)
z = pushBack(z, 13, 17)
z = pushBack(z, 12, 13)
