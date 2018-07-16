import collections

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        q = collections.deque()
        for i, num in enumerate(nums):
            if num == 0:
                q.append(i)
            elif q:
                index_0 = q.popleft()
                nums[i], nums[index_0] = nums[index_0], nums[i]
                q.append(i)