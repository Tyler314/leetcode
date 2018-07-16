class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        maxx = 0
        memo = set()
        for num in nums:
            memo.add(num)
        for num in nums:
            if num - 1 not in memo:
                cnt = 0
                while num + cnt in memo:
                    cnt += 1
                if cnt > maxx:
                    maxx = cnt
        return maxx