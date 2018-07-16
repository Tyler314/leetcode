class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def _binSearch(left, right):
            if left > right:
                return -1
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return _binSearch(left, mid - 1)
            return _binSearch(mid + 1, right)
        if nums == []:
            return [-1, -1]
        index = _binSearch(0, len(nums) - 1)
        if index == -1:
            return [-1, -1]
        i = j = index
        while -1 < i and nums[i] == target:
            i -= 1
        while j < len(nums) and nums[j] == target:
            j += 1
        return [i + 1, j - 1]