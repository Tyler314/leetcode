# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
import sys

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = collections.deque()
        q.append((root, (-sys.maxsize - 1, sys.maxsize)))
        while q:
            curr, bounds = q.popleft()
            lower, upper = bounds
            if not (lower < curr.val < upper):
                return False
            if curr.left:
                q.append((curr.left, (lower, curr.val)))
            if curr.right:    
                q.append((curr.right, (curr.val, upper)))
        return True