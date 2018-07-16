class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = [None, '1', '11', '21']
        if n < 4:
            return nums[n]
        for i in range(4, n+1):
            cnt = 0
            curr = None
            new_word = ''
            for d in nums[-1]:
                if curr is None:
                    curr = d
                    cnt = 1
                elif d == curr:
                    cnt += 1
                else:
                    new_word += str(cnt) + curr
                    curr = d
                    cnt = 1
            new_word += str(cnt) + curr
            nums.append(new_word)
        return nums[-1]