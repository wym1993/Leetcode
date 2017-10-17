from collections import defaultdict
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(int)
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.store[timestamp]+=1;
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for i in range(timestamp-299, timestamp+1):
            res+=self.store.get(i, 0)
        return res;
                
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)