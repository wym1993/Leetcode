class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)/2+1):
            if len(s)%i!=0:
                continue;
            
            t = len(s)/i
            test = [str(s[start*i:(start+1)*i]) for start in range(t)];
            if len(list(set(test)))==1:
                return True;
        
        return False;