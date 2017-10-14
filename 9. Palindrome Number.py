class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x == 0:
            return True;
        
        num = 0;
        step = 1;
        while step<=x:
            num+=1;
            step*=10;
        
        l = step/10;
        r = 1;
        while(l>r):
            ldigit = (x/l)%10;
            rdigit = (x/r)%10;
            if ldigit!=rdigit:
                return False;
            else:
                l/=10;
                r*=10;
        
        return True;
        
    