class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0;
        res = 0;

        while start<len(s):
            end = start+1;
            while end<len(s) and s[end]==s[end-1]:
                end+=1;

            second, end = end, end+1;
            while end<len(s) and s[end]==s[end-1]:
                end+=1;

            #print s[start:second],s[second:end]
            res+=min(len(s[start:second]), len(s[second:end]))

            start = second;

        return res;
