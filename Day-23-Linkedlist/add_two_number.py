class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_reverse_linkedlist(num):
    start = head = Node(num%10)
    num = num//10
    while num:
        head.next = Node(num%10)
        num = num // 10
        head = head.next
    return start


def traverse_linkedlist(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


def add_two_numbers(lnum1, lnum2):
    result = start = Node(None)
    carry = 0

    while lnum1 or lnum2 or carry:
        if lnum1:
            carry += lnum1.data
            lnum1 = lnum1.next
        if lnum2:
            carry += lnum2.data
            lnum2 = lnum2.next
        result.next = Node(carry%10)
        result = result.next
        carry = carry//10
    return start.next


if __name__ == '__main__':
    num1 = 9876
    num2 = 876452
    lnum1 = create_reverse_linkedlist(num1)
    lnum2 = create_reverse_linkedlist(num2)
    traverse_linkedlist(lnum1)
    traverse_linkedlist(lnum2)
    output = add_two_numbers(lnum1, lnum2)
    traverse_linkedlist(output)