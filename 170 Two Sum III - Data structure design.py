class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {};
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if not number in self.store:
            self.store[number] = 1;
        else:
            self.store[number]+=1;

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.store:
            num = value-key;
            if (num!=key and num in self.store) or (num==key and self.store[key]>1):
                return True;
        return False;


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)