import itertools

class Solution:
    def __init__(self):
        self.lookup = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        perms = []
        for perm in itertools.product(*[self.lookup[digit] for digit in digits]):
            perms.append(''.join(perm))
        return perms