class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        comp = {'1':'1', '0':'0', '6':'9', '9':'6', '8':'8'}
        l = len(num)-1
        for i, c in enumerate(num):
            if c not in comp.keys():
                return False;
            if num[l-i]!=comp[c]:
                return False;
            
            if i>l/2:
                break;
        return True;
            