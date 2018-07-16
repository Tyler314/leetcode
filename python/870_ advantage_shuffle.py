class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        def _findClosest(nums, elem, i):
            elem += 1
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = left + ((right - left) // 2)
                if nums[mid] == elem:
                    nums.pop(mid)
                    return elem
                if nums[mid] > elem:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[left] > B[i]:
                return nums.pop(left)
            if left + 1 < len(nums) and nums[left + 1] > B[i]:
                return nums.pop(left + 1)
            return nums.pop(0)
        a = sorted(A)
        ret = []
        for i, elem in enumerate(B):
            ret.append(_findClosest(a, elem, i))
        return ret