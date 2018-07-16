class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums) - 1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
        if len(nums) > 1 and nums[-1] > nums[-2]:
            return len(nums) - 1
        return 0