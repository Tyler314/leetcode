import numpy as np

class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        row = [0 for _ in range(len(grid))]
        col = [0 for _ in range(len(grid[0]))]
        for i, r in enumerate(grid):
            for j, elem in enumerate(r):
                if elem != 0:
                    cnt += 1
                if row[i] < elem:
                    row[i] = elem
                if col[j] < elem:
                    col[j] = elem
        return cnt + sum(row) + sum(col)
    
    def projectionAreaNumpy(self, grid):
        """
        Solved using numpy
        """
        grid = np.asarray(grid)
        return np.count_nonzero(grid) + sum([max(grid[row,:]) for row in range(len(grid))]) + sum([max(grid[:,col]) for col in range(len(grid[0]))])