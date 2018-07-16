class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))
        """
        even_sum = odd_sum = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_sum = max(even_sum + num, odd_sum)
            else:
                odd_sum  = max(odd_sum  + num, even_sum)
        return max(even_sum, odd_sum)