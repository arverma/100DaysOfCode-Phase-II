__author__ = 'aman.rv'

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_temp = l1.val + l2.val
        carry = sum_temp // 10
        ans = ListNode(sum_temp % 10)
        head = ans
        l1 = l1.next
        l2 = l2.next
        while l1 or l2 or carry:
            sum_temp = carry
            if l1:
                sum_temp += l1.val
                l1 = l1.next
            if l2:
                sum_temp += l2.val
                l2 = l2.next
            carry = sum_temp // 10
            ans.next = ListNode(sum_temp % 10)
            ans = ans.next
        return head

