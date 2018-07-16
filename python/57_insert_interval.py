# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import sys

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def _inbetween(a, b):
            return a.end < newInterval.start and newInterval.end < b.start
        def _overLap(a, b):
            return (a.start <= b.end and a.end >= b.end) or (a.end >= b.start and a.end <= b.end) or (a.start <= b.start and a.end >= b.end)
        def _insertInterval(interval, i):
            nonlocal intervals
            interval = Interval(min(interval.start, intervals[i].start), max(interval.end, intervals[i].end))
            overlaps_everything = True
            for j in range(i + 1, len(intervals)):
                if _overLap(intervals[j], interval):
                    interval = Interval(min(interval.start, intervals[j].start), max(interval.end, intervals[j].end))
                else:
                    overlaps_everything = False
                    break
            intervals[i] = interval
            if i != len(intervals) - 1:
                if overlaps_everything:
                    intervals = intervals[:i+1]
                else:
                    intervals = intervals[:i+1] + intervals[j:]
        prev = Interval(-sys.maxsize - 1, -sys.maxsize - 1)
        for i, curr_interval in enumerate(intervals):
            if _inbetween(prev, curr_interval):
                intervals.insert(i, newInterval)
                return intervals
            if _overLap(curr_interval, newInterval):
                _insertInterval(newInterval, i)
                return intervals
        intervals.append(newInterval)
        return intervals