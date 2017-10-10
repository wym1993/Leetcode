# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        from collections import defaultdict
        store = defaultdict(int)
        for interval in intervals:
            store[interval.start]+=1;
            store[interval.end]-=1;
            
        m, curr = 0, 0
        #print sorted(store.items(), key = lambda x:x[0])
        for node, dir in sorted(store.items(), key = lambda x:x[0]):
            curr+=dir;
            m = max(m, curr);
        
        return m