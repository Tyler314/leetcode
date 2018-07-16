class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        for i, elem in enumerate(nums):
            if i == len(nums) - 1:
                return True
            if elem == 0:
                j = i - 1
                found = False
                while j >= 0:
                    if nums[j] >= i - j + 1:
                        found = True
                        break
                    j -= 1
                if not found:
                    return False
        return True