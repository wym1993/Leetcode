class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        
        s.reverse();
        
        idx = 0;
        for i in range(len(s)):
            if s[i]==" ":
                s[idx:i] = reversed(s[idx:i]);
                idx = i+1;
        
        s[idx:] = reversed(s[idx:]);