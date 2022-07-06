class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lot_top_to_bottom_left_to_right(root):
    queue = [root]
    while len(queue) > 0:
        p_node = queue.pop(0)
        print(p_node.data, end=" ")
        if p_node.left:
            queue.append(p_node.left)
        if p_node.right:
            queue.append(p_node.right)


def lot_top_to_bottom_right_to_left(root):
    queue = [root]
    while len(queue) > 0:
        p_node = queue.pop(0)
        print(p_node.data, end=" ")
        if p_node.right:
            queue.append(p_node.right)
        if p_node.left:
            queue.append(p_node.left)


def lot_bottom_to_top_right_to_left(root):
    queue = [root]
    stack = []
    while len(queue) > 0:
        p_node = queue.pop(0)
        stack.append(p_node.data)
        if p_node.left:
            queue.append(p_node.left)
        if p_node.right:
            queue.append(p_node.right)
    while len(stack) > 0:
        print(stack.pop(), end=" ")


def lot_bottom_to_top_left_to_right(root):
    queue = [root]
    stack = []
    while len(queue) > 0:
        p_node = queue.pop(0)
        stack.append(p_node.data)
        if p_node.right:
            queue.append(p_node.right)
        if p_node.left:
            queue.append(p_node.left)
    while len(stack) > 0:
        print(stack.pop(), end=" ")


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(7)

    lot_top_to_bottom_left_to_right(root)
    print()
    lot_top_to_bottom_right_to_left(root)
    print()
    lot_bottom_to_top_left_to_right(root)
    print()
    lot_bottom_to_top_right_to_left(root)
