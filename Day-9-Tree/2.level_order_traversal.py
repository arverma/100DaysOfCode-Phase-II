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


def level_order_utils_up_down_left_right(q, res):
    if len(q) >= 1:
        r = q[0]
        res.append(r.data)
        if r.left:
            q.append(r.left)
        if r.right:
            q.append(r.right)
        level_order_utils_up_down_left_right(q[1::], res)
    return res


def level_order_utils_down_up_right_left(q, res):
    if len(q) >= 1:
        r = q[0]
        res.append(r.data)
        if r.left:
            q.append(r.left)
        if r.right:
            q.append(r.right)
        level_order_utils_down_up_right_left(q[1::], res)
    return res[::-1]


def level_order_utils_up_down_right_left(q, res):
    if len(q) >= 1:
        r = q[0]
        res.append(r.data)
        if r.right:
            q.append(r.right)
        if r.left:
            q.append(r.left)
        level_order_utils_up_down_right_left(q[1::], res)
    return res


def level_order_utils_down_up_left_right(q, res):
    if len(q) >= 1:
        r = q[0]
        res.append(r.data)
        if r.right:
            q.append(r.right)
        if r.left:
            q.append(r.left)
        level_order_utils_down_up_left_right(q[1::], res)
    return res[::-1]


def level_order_utils_up_down_zig_zag(s1, s2, res, flag):
    # print([i.data for i in s1], [j.data for j in s2])
    if len(s1) > 0 or len(s2) > 0:
        if len(s1) > 0 and flag == 1:
            r = s1.pop()
            res.append(r.data)
            if r.left:
                s2.append(r.left)
            if r.right:
                s2.append(r.right)
            level_order_utils_up_down_zig_zag(s1, s2, res, flag)
        elif flag == 1:
            level_order_utils_up_down_zig_zag(s1, s2, res, 0)

        if len(s2) > 0 and flag == 0:
            r = s2.pop()
            res.append(r.data)
            if r.right:
                s1.append(r.right)
            if r.left:
                s1.append(r.left)
            level_order_utils_up_down_zig_zag(s1, s2, res, flag)
        elif flag == 0:
            level_order_utils_up_down_zig_zag(s1, s2, res, 1)
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
            print("LEVEL ORDER UP DOWN LEFT RIGHT:", level_order_utils_up_down_left_right([self.root], []))
            print("LEVEL ORDER UP DOWN RIGHT LEFT:", level_order_utils_up_down_right_left([self.root], []))
            print("LEVEL ORDER DOWN UP RIGHT LEFT:", level_order_utils_down_up_right_left([self.root], []))
            print("LEVEL ORDER DOWN UP LEFT RIGHT:", level_order_utils_down_up_left_right([self.root], []))
            print("LEVEL ORDER UP DOWN ZIG ZAG:", level_order_utils_up_down_zig_zag([self.root], [], [], 1))

    def insert(self, value):
        insert_utils(self.root, value)


if __name__ == '__main__':
    a = [1, 2, 4, 4, 3, -6, 0, -9, -8, 15, 7, 8]
    traversal = Traversal(a[0])
    for i in a[1::]:
        traversal.insert(i)
    traversal.level_order()
