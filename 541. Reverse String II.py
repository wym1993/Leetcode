class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ''
        start = 0;
        while start<len(s):
            end = start+k if start+k<len(s) else len(s);
            result+=s[start:end][::-1];
            start+=k;
            end = start+k if start+k<len(s) else len(s);
            result+=s[start:end];
            start+=k;
        
        return result;
            