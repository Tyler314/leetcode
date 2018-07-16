class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        _sum = 0
        while i < len(s):
            if i == len(s) - 1:
                _sum += m[s[i]]
            elif s[i:i+2] == 'IV':
                _sum += 4
                i += 1
            elif s[i:i+2] == 'IX':
                _sum += 9
                i += 1
            elif s[i:i+2] == 'XL':
                _sum += 40
                i += 1
            elif s[i:i+2] == 'XC':
                _sum += 90
                i += 1
            elif s[i:i+2] == 'CD':
                _sum += 400
                i += 1
            elif s[i:i+2] == 'CM':
                _sum += 900
                i += 1
            else:
                _sum += m[s[i]]
            i += 1
        return _sum