class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True;
        
        l = 0;
        r = len(s)-1;
        while l<r:
            while l<r and not s[l].isalpha() and not s[l].isdigit():
                l+=1;
            while l<r and not s[r].isalpha() and not s[r].isdigit():
                r-=1;
            
            if l<r and s[l].lower() !=s[r].lower():
                return False;
            
            l+=1;
            r-=1;
        
        return True;
            
        
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        news = [c.lower() for c in s if c.isalnum()];
        return news==news[::-1];