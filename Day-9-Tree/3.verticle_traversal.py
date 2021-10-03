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


def vertical_order_utils(q, res):
    if len(q) > 0:
        r = q[0][0]
        hd = q[0][1]
        res[hd] = res.get(hd, []) + [r.data]
        if r.left:
            q.append([r.left, hd-1])
        if r.right:
            q.append([r.right, hd+1])
        vertical_order_utils(q[1::], res)
    return res


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
            print("LEVEL ORDER UP DOWN LEFT RIGHT:", vertical_order_utils([[self.root, 0]], {}))

    def insert(self, value):
        insert_utils(self.root, value)


if __name__ == '__main__':
    a = [1, 2, 4, 4, 3, -6, 0, -9, -8, 15, 7, 8]
    traversal = Traversal(a[0])
    for i in a[1::]:
        traversal.insert(i)
    traversal.level_order()
