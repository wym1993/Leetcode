class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i  = len(s)-2;
        roman = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000};
        total =roman[s[-1]];
        
        while i>=0:
            if roman[s[i]]<roman[s[i+1]]:
                total-=roman[s[i]];
            else:
                total+=roman[s[i]];
            i-=1;
        
        return total;