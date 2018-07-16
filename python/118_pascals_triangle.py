class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ret = [[1]]
        for i in range(1, numRows):
            tmp = []
            for j in range(i + 1):
                if j == 0:
                    tmp.append(ret[i - 1][j])
                elif j == i:
                    tmp.append(ret[i - 1][j - 1])
                else:
                    tmp.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(tmp)
        return ret