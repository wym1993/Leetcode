class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0;
        split = s.split(' ')
        while split and not split[-1]:
            split.pop();
        
        return len(split[-1]) if split else 0;
        