from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i, j, l = 0, 0, 0
        store = defaultdict(int);
        while j<len(s):
            store[s[j]]+=1;
            if len(store.keys())>k:
                while i<j:
                    if store[s[i]]==1:
                        del store[s[i]];
                        i+=1
                        break;
                    else:
                        store[s[i]]-=1;
                        i+=1;
            if len(store.keys())<=k:
                l = max(l, sum(store.values()));
            
            j+=1;
        
        return l
                        
        