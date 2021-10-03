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


def diameter_of_a_tree_utils(r):
    if r is None:
        return 0, 0
    lh = diameter_of_a_tree_utils(r.left)[1]
    rh = diameter_of_a_tree_utils(r.right)[1]
    diameter = 1 + lh + rh
    return diameter, 1 + max(lh, rh)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Traversal:
    def __init__(self, data):
        self.root = Node(data)

    def level_order(self):
        if self.root:
            print("Find diameter of a tree:", diameter_of_a_tree_utils(self.root)[0])

    def insert(self, value):
        insert_utils(self.root, value)


if __name__ == '__main__':
    a = [1, 2, 4, 4, 3, -6, 0, -9, -8, 15, 7, 8]
    traversal = Traversal(a[0])
    for i in a[1::]:
        traversal.insert(i)
    traversal.level_order()
