class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        ret = []
        top_row = left_col = 0
        bottom_row = len(matrix) - 1
        right_col = len(matrix[0]) - 1
        
        while True:
            for i in range(left_col, right_col + 1):
                ret.append(matrix[top_row][i])
            top_row += 1
            if self._done(top_row, bottom_row, left_col, right_col):
                break
            for i in range(top_row, bottom_row + 1):
                ret.append(matrix[i][right_col])
            right_col -= 1
            if self._done(top_row, bottom_row, left_col, right_col):
                break
            for i in range(right_col, left_col - 1, -1):
                ret.append(matrix[bottom_row][i])
            bottom_row -= 1
            if self._done(top_row, bottom_row, left_col, right_col):
                break
            for i in range(bottom_row, top_row - 1, -1):
                ret.append(matrix[i][left_col])
            left_col += 1  
            if self._done(top_row, bottom_row, left_col, right_col):
                break
        return ret
                
    def _done(self, top, bottom, left, right):
        return top > bottom or left > right