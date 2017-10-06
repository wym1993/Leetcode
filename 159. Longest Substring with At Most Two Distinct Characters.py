from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0;
        l = 0
        store = defaultdict(int);
        start = 0;
        for i, c in enumerate(s):
            store[c]+=1;
            if len(store.keys())<=2:
                l = max(l, i-start+1);
            else:
                l = max(l, i-start);
                while start<i and len(store.keys())>2:
                    if store[s[start]]==1:
                        del store[s[start]];
                        start+=1;
                        break;
                    else:
                        store[s[start]]-=1;
                        start+=1;
        
        if len(store.keys())<=2:
            l = max(l, len(s)-start)
        
        return l;