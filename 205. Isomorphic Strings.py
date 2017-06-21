class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sVals = self.getVal(s);
        tVals = self.getVal(t);
        return sorted(sVals)==sorted(tVals);
    
    def getVal(self, s):
        store = {};
        for i, c in enumerate(s):
            if not c in store:
                store[c] = [i];
            else:
                store[c].append(i);
        
        return store.values();

def isIsomorphic3(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))