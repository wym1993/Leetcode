class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        store = {};
        for i in range(len(s)-9):
            store[s[i:i+10]] = store.get(s[i:i+10], 0)+1;
        return [key for key in store.keys() if store[key]>1];