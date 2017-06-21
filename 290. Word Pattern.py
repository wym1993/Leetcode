class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split();
        if len(strList)!=len(pattern):
            return False;
        store1 = {};
        store2 = {};
        
        for i in range(len(pattern)):
            if pattern[i] in store1:
                if store1[pattern[i]]!=strList[i]:
                    return False;
            else:
                store1[pattern[i]] = strList[i];
            
            if strList[i] in store2:
                if store2[strList[i]]!=pattern[i]:
                    return False;
            else:
                store2[strList[i]] = pattern[i];
        
        return True;




class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pVals = self.checkVal(pattern);
        sVals = self.checkVal(str.split(' '));
        print pVals, sVals
        return sorted(pVals)==sorted(sVals);
    
    def checkVal(s, vals):
        store = {};
        for i, val in enumerate(vals):
            if not val in store:
                store[val] = [i];
            else:
                store[val].append(i)
        
        return store.values();