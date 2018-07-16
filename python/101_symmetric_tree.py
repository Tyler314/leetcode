# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == []:
            return False
        q = collections.deque()
        level_order = [[]]
        q.append((root, 0))
        while q:
            curr, level = q.popleft()
            while len(level_order) <= level:
                level_order.append([])
            if curr is None:
                level_order[level].append(None)
            else:
                level_order[level].append(curr.val)
            if curr is not None:
                q.append((curr.left,  level + 1))
                q.append((curr.right, level + 1))
        for queue in level_order:
            for i in range(len(queue) // 2):
                if queue[i] != queue[-1 - i]:
                    return False
        return True