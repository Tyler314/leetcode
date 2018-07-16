import sys

class Solution:
    def __init__(self):
        self._min = sys.maxsize
        self.memo = dict()
        self.triangle = None
        
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.triangle = triangle
        return self._findMinPath(0,0)
        
    def _findMinPath(self, i, j):
        if i + 1 == len(self.triangle):
            return self.triangle[i][j]
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        tmp = sys.maxsize
        for k in [j, j + 1]:
            tmp = min(tmp, self.triangle[i][j] + self._findMinPath(i + 1, k))
        self.memo[(i,j)] = tmp
        return tmp