from collections import Counter
from collections import defaultdict
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words or k<1:
            return [];
        
        counter = Counter(words);

        rev_counter = defaultdict(list)
        for key, val in counter.items():
            rev_counter[val].append(key);
        
        i = max(rev_counter.keys());
        res = []
        while i>0 and len(res)<min(len(words), k):
            if i in rev_counter.keys():
                curr = sorted(rev_counter[i]);
                res+=curr;
            i-=1;
        
        return res[:k];
                
        
            