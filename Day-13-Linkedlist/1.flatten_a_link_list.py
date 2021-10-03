# https://www.geeksforgeeks.org/flattening-a-linked-list/

class MainNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.down = None


class SimpleNode:
    def __init__(self, data):
        self.data = data
        self.down = None


class LinkedList:
    def __init__(self):
        self.head = None  # Original 2D Linked list
        self.root = None  # Sorted Linked List

    def construct_2d_linked_list(self, a):
        self.head = MainNode(a[0][0])
        start = self.head
        middle = self.head
        for i, x in enumerate(a):
            for y in x[1::]:
                start.down = SimpleNode(y)
                start = start.down
            if i < len(a) - 1:
                middle.next = MainNode(a[i + 1][0])
                start = middle.next
                middle = middle.next

    def traverse(self):
        right = self.head
        while right:
            down = right
            while down:
                print(down.data, end=" ")
                down = down.down
            right = right.next

    def sorted_traverse(self):
        h = self.head
        self.root = SimpleNode(-100)
        while h:
            self.merge(h)
            h = h.next
        sl = self.root.down
        while sl:
            print(sl.data, end=" ")
            sl = sl.down

    def merge(self, a):
        b = self.root
        r = SimpleNode(-100)
        temp = r
        while a and b:
            if a.data > b.data:
                temp.down = SimpleNode(b.data)
                b = b.down
            else:
                temp.down = SimpleNode(a.data)
                a = a.down
            temp = temp.down
        if a:
            temp.down = a
        else:
            temp.down = b
        self.root = r.down


if __name__ == '__main__':
    a = [[-11, 20, 33, 41, 53], [8, 26, 61, 63], [10], [22, 27, 61, 62]]
    ll = LinkedList()
    ll.construct_2d_linked_list(a)
    print("Simple Traverse")
    ll.traverse()
    print()
    print("Sorted Traverse")
    ll.sorted_traverse()
