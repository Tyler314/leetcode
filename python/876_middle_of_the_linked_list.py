# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        itr = fast_itr = head
        while fast_itr:
            if not fast_itr.next:
                break
            itr = itr.next
            fast_itr = fast_itr.next.next
        return itr