class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ret = [1 for _ in range(len(ratings))]
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1] and ret[i] >= ret[i + 1]:
                ret[i + 1] = ret[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] < ratings[i - 1] and ret[i] >= ret[i - 1]:
                ret[i - 1] = ret[i] + 1
        return sum(ret)