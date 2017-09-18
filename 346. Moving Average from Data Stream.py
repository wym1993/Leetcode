class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size;
        self.store = [0];
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.store.append(self.store[-1]+val);
        if len(self.store)<self.size+1:
            return self.store[-1]/(len(self.store)-1.0);
        else:
            return (self.store[-1]-self.store[-1-self.size])*1.0/self.size;
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)