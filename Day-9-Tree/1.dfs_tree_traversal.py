# DFS: Depth First Search

def insert_utils(r, value):
    if value > r.data and r.right:
        insert_utils(r.right, value)
    elif value < r.data and r.left:
        insert_utils(r.left, value)
    elif value > r.data and r.right is None:
        r.right = Node(value)
    elif value < r.data and r.left is None:
        r.left = Node(value)


def inorder_utils(r, res):
    if r:
        inorder_utils(r.left, res)
        res.append(r.data)
        inorder_utils(r.right, res)
    return res


def preorder_utils(r, res):
    if r:
        res.append(r.data)
        preorder_utils(r.left, res)
        preorder_utils(r.right, res)
    return res


def postorder_utils(r, res):
    if r:
        postorder_utils(r.left, res)
        postorder_utils(r.right, res)
        res.append(r.data)
    return res


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Traversal:
    def __init__(self, data):
        self.root = Node(data)

    def inorder(self):
        print("INORDER:", inorder_utils(self.root, []))

    def postorder(self):
        print("POSTORDER:", postorder_utils(self.root, []))

    def preorder(self):
        print("PREORDER:", preorder_utils(self.root, []))

    def insert(self, value):
        insert_utils(self.root, value)


if __name__ == '__main__':
    a = [1, 2, 4, 4, 3, -6, 0, -9, -8, 15, 7, 8]
    traversal = Traversal(a[0])
    for i in a[1::]:
        traversal.insert(i)
    traversal.inorder()
    traversal.preorder()
    traversal.postorder()
