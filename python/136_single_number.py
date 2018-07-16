from collections import Counter

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = Counter()
        for num in nums:
            memo[num] += 1
        for num in memo:
            if memo[num] == 1:
                return num