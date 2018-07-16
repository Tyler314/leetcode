class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        wordDict.add("")
        memo = dict()
        def _canBreak(word):
            if word in memo:
                return memo[word]
            if word in wordDict:
                return True
            for i in range(len(word)):
                if word[:i+1] in wordDict and word[:i+1] not in memo:
                    if _canBreak(word[i+1:]):
                        memo[word[i+1:]] = True
                        return True
                    else:
                        memo[word[i+1:]] = False
            return False
        return _canBreak(s)