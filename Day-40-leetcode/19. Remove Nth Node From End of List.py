__author__ = 'aman.rv'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        link = head
        while link:
            link = link.next
            length += 1

        n = length - n
        link = head
        if n <= 0:
            return head.next
        while n > 1:
            head = head.next
            n -= 1
        head.next = head.next.next
        return link

