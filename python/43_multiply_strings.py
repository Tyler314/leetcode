class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        external_shift = 1
        for char1 in reversed(num1):
            tmp = 0
            internal_shift = 1
            for char2 in reversed(num2):
                tmp += int(char1) * int(char2) * internal_shift
                internal_shift *= 10
            res += tmp * external_shift
            external_shift *= 10
        return str(res)