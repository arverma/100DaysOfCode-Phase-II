class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_utils(r, data):
    pass


def left_view_utils(r):
    pass


class Traversal:
    def __init__(self, data):
        self.root = Node(data=data)

    def insert(self, data):
        insert_utils(self.root, data)

    def left_view(self):
        print(left_view_utils(self.root))


if __name__ == '__main__':
    a = [1, 2, 4, 4, 3, -6, 0, -9, -8, 15, 7, 8]
    t = Traversal(a[0])

    for i in a[1::]:
        t.insert(i)
    t.left_view()