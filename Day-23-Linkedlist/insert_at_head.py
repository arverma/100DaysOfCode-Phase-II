class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def traverse_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == '__main__':
    arr = [-10, -20, 30, 0]
    head = None
    for a in arr:
        head = insert_at_head(head, a)
        traverse_linked_list(head)
