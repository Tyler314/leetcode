class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        longest = 0
        memo = dict()
        i = 0
        while i < len(s):
            char = s[i]
            if char not in memo:
                memo[char] = i
                cnt += 1
            else:
                longest = max(longest, cnt)
                i = memo[char]
                memo.clear()
                cnt = 0
            i += 1
        return max(longest, cnt)