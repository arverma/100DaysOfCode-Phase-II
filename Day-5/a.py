import heapq


class Node:
    def __init__(self, head):
        self.head = head
        self.next = None


def heap():
    a = [100,2,3,4,5]
    heapq.heapify(a)
    print(a)
    print(heapq.heappop(a))
    print(a)
    print(heapq.nlargest(2, a))
    pass


def back_tracking(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            back_tracking(s, l + 1, r)
            s[l], s[i] = s[i], s[l]


def balanced_parenthesis(s, n, o, c):
    if len(s) == 2*n:
        print(s)
    else:
        if o > c:
            balanced_parenthesis(s + ")", n, o, c + 1)
        if o < n:
            balanced_parenthesis(s + "(", n, o + 1, c)


if __name__ == '__main__':
    n = 3
    # balanced_parenthesis("", n, 0, 0)
    heap()