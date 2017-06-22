class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        store = {};
        for c in s:
            store[c] = store.get(c, 0)+1;
        
        for c in t:
            if not c in store or store[c]==0:
                return c;
            else:
                store[c]-=1;


class Solution(object):
    def findTheDifference(self, s, t):
        return chr(reduce(operator.xor, map(ord, s + t)))