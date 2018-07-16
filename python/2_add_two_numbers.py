# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return [int(i) for i in reversed(str(self._sum(l1) + self._sum(l2)))]
    
    def _sum(self, root):
        carry = 0
        summ = 0
        place = 1
        while root:
            summ += root.val * place
            place *= 10
            root = root.next
        return summ