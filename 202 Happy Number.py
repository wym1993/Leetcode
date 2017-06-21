class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        store = [];
        sum = n;
        while sum!=1:
            temp = 0;
            while sum>0:
                temp+=(sum%10)*(sum%10);
                sum/=10;
            sum = temp;
            if sum in store:
                return False;
            else:
                store.append(sum);
        
        return True;