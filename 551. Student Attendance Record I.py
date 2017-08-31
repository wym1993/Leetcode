import collections
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = collections.Counter(s);
        return counter['A']<=1 and 'LLL' not in s
    
        