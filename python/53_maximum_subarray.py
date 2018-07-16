class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = nums[0]
        for i, elem in enumerate(nums[1:]):
            a = max(elem, a + elem)
            b = max(b, a)
        return b