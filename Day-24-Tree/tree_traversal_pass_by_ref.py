class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(root, arr):
    if root is None:
        return
    arr.append(root.data)
    preorder_traversal(root.left, arr)
    preorder_traversal(root.right, arr)


def inorder_traversal(root, arr):
    if root is None:
        return
    inorder_traversal(root.left, arr)
    arr.append(root.data)
    inorder_traversal(root.right, arr)


def post_order_traversal(root, arr):
    if root is None:
        return
    post_order_traversal(root.left, arr)
    post_order_traversal(root.right, arr)
    arr.append(root.data)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(7)

    arr = []
    preorder_traversal(root, arr)
    print(arr)
    arr = []
    inorder_traversal(root, arr)
    print(arr)
    arr = []
    post_order_traversal(root, arr)
    print(arr)