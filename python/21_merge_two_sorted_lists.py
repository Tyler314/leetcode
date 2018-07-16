# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        l1itr = l1
        l2itr = l2
        if l1itr.val > l2itr.val:
            ret = ListNode(l2itr.val)
            l2itr = l2itr.next
        else:
            ret = ListNode(l1itr.val)
            l1itr = l1itr.next
        itr = ret
        while l1itr and l2itr:
            if l1itr.val > l2itr.val:
                itr.next = ListNode(l2itr.val)
                l2itr = l2itr.next
            else:
                itr.next = ListNode(l1itr.val)
                l1itr = l1itr.next
            itr = itr.next
        while l1itr:
            itr.next = ListNode(l1itr.val)
            itr = itr.next
            l1itr = l1itr.next
        while l2itr:
            itr.next = ListNode(l2itr.val)
            itr = itr.next
            l2itr = l2itr.next
        return ret