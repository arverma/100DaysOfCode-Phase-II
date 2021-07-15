#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
# from Queue import PriorityQueue


class Node:
    def __init__(self, Value) -> None:
        self.val = Value
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = Node(0)
        q = PriorityQueue()
        for i, l in enumerate(lists):
            if l:
                q.put((l.val, i, l))

        while not q.empty():
            val, id, node = q.get()
            point.next = Node(val)
            point = point.next
            node = node.next
            if node:
                i += 1
                q.put((node.val, i, node))
        return head.next
# @lc code=end
