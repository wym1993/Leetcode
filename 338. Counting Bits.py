class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        while len(result)<=num:
            tmp = [i+1 for i in result];
            result+=tmp;
        
        return result[:(num+1)];