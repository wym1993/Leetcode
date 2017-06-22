from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dist_words = list(set(s));
        coun = Counter(s);
        result = 0;
        hasUsed = False;
        for c in dist_words:
            if coun[c]%2==0:
                result+=coun[c];
            else:
                if coun[c]/2>=1:
                    result+=int(coun[c]/2)*2;
                if not hasUsed:
                    hasUsed = True;
                    result+=1;
        
        return result;
        