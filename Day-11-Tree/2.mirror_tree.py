class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_utils(r, res):
    if r:
        inorder_utils(r.left, res)
        res.append(r.data)
        inorder_utils(r.right, res)
    return res


def insert_utils(r, value):
    if value > r.data and r.right:
        insert_utils(r.right, value)
    elif value < r.data and r.left:
        insert_utils(r.left, value)
    elif value > r.data and r.right is None:
        r.right = Node(value)
    elif value < r.data and r.left is None:
        r.left = Node(value)


def generate_mirror_utils(r):
    if r:
        r.left, r.right = r.right, r.left
        generate_mirror_utils(r.left)
        generate_mirror_utils(r.right)


class Traversal:
    def __init__(self, data):
        self.root = Node(data=data)

    def inorder(self):
        print("INORDER:", inorder_utils(self.root, []))

    def insert(self, data):
        insert_utils(self.root, data)

    def generate_mirror(self):
        generate_mirror_utils(self.root)


if __name__ == '__main__':
    a = [1, 2, 4, 4, 3, -6, 0, -9, -8, 15, 7, 8]
    t = Traversal(a[0])

    for i in a[1::]:
        t.insert(i)
    t.inorder()
    t.generate_mirror()
    t.inorder()