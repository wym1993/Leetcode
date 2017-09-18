class Solution:
    """
    @param: num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        if not num:
            return True;
        comp = {'6':'9', '9':'6', '1':'1', '8':'8', '0':'0'}
        
        i, j = 0, len(num)-1
        while i<=j:
            if not num[i] in comp.keys() or num[j]!=comp[num[i]]:
                return False;
            else:
                i, j = i+1, j-1;
        
        return True;