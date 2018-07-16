# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import copy

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda interval: interval.start)
        ret = []
        memo = set()
        for i, interval in enumerate(intervals):
            if i in memo:
                continue
            tmp = copy.copy(interval)
            for j in range(i+1, len(intervals)):
                if (not (self._smallerThan(tmp, intervals[j]) or self._smallerThan(intervals[j], tmp))) and not j in memo:
                    tmp.start = min(tmp.start, intervals[j].start)
                    tmp.end   = max(tmp.end,   intervals[j].end)
                    memo.add(j)
                else:
                    break
            ret.append(tmp)
        return ret
            
    def _smallerThan(self, a, b):
        return a.start < b.start and a.start < b.end and a.end < b.start and a.end < b.end