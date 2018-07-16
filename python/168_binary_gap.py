class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)[2:]
        gap = 0
        curr = 0
        for bit in b:
            if bit == '1':
                gap = max(gap, curr)
                curr = 1
            else:
                curr += 1
        return gap