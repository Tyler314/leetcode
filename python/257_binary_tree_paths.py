# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.paths = []
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            self._bfs(root)
        return self.paths
        
    def _bfs(self, node, path=''):
        path += str(node.val) + "->"
        if node.left:
            self._bfs(node.left, path)
        if node.right:
            self._bfs(node.right, path)
        if not node.left and not node.right:
            self.paths.append(path.rstrip('->'))