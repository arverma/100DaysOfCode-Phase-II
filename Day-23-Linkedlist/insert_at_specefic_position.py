class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(arr):
    head = Node(arr[0])
    start = head
    for a in arr[1::]:
        head.next = Node(a)
        head = head.next
    return start


def insert_at_position(head, pos, data):
    if pos == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node

    start = head
    i = 0
    while i < pos-1:
        head = head.next
        i += 1
    after_node = head.next
    head.next = Node(data)
    head = head.next
    head.next = after_node
    return start


def traverse_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == '__main__':
    arr = [12, 2, 5, 0, -1]
    head = create_linked_list(arr)
    traverse_linked_list(head)
    insert = ((0, -100), (3, -100), (5, -100), (1, -100), (4, -100))
    for i in insert:
        head = insert_at_position(head, i[0], i[1])
        traverse_linked_list(head)

