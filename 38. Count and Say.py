class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return "";
        result = "1";
        if n==1:
            return result;
        
        for i in range(2,n+1):
            temp = ""; j=0;
            while j<len(result):
                count = 0; digit = result[j]; 
                while j<len(result) and result[j]==digit:
                    count+=1;
                    j+=1;
                temp+= str(count) + digit;
            
            result = temp;
        
        return result;

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s