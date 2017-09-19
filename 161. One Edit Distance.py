class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hasChange = False;
        i, j = 0, 0;
        while i<len(s) and j<len(t):
            if s[i]!=t[j]:
                if hasChange:
                    return False;
                else:
                    hasChange=True;
                    if len(s)==len(t):
                        i+=1;
                        j+=1;
                    else:
                        if len(s)<len(t):
                            j+=1;
                        else:
                            i+=1;
            else:
                i+=1;
                j+=1;
        
        if hasChange:
            return i==len(s) and j==len(t);
        else:
            return abs(len(s)-len(t))==1


class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if they are both one edit distance apart or false
    def isOneEditDistance(self, s, t):
        # Write your code here
        m = len(s)
        n = len(t)
        if abs(m - n) > 1:
            return False

        if m > n:
            return self.isOneEditDistance(t, s)

        for i in xrange(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                return s[i:] == t[i + 1:]

        return m != n