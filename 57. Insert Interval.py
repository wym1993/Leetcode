# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval);
        return self.merge(intervals);
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return [];
        intervals = sorted(intervals, key = lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end;
        result = []
        for interval in intervals[1:]:
            if interval.start>end:
                result.append([start, end]);
                start, end = interval.start, interval.end;
            else:
                start, end = min(start, interval.start), max(end, interval.end);
        
        result.append([start, end]);
        return result;


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start, end = newInterval.start, newInterval.end;
        result = [];
        for interval in intervals:
            if interval.end<start:
                result.append(interval);
            elif interval.start>end:
                result.append(Interval(start, end));
                start, end = interval.start, interval.end;
            else:
                start, end = min(start, interval.start), max(end, interval.end);
        
        result.append(Interval(start, end));
        return result;