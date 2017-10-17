class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        key = sorted(list(set([i for [i, n] in people])), reverse = True);
        store = {};
        for h in key:
            store[h] = 0
        
        def helper(cands, curr, key, store):
            if not cands:
                return curr;
            
            for idx, [h, n] in enumerate(cands):
                if n>len(curr):
                    continue;
                num = 0
                for i in range(key.index(h)+1):
                    num+=store[key[i]];
                if n==num:
                    store[h]+=1
                    res = helper(cands[:idx]+cands[idx+1:], curr+[[h, n]], key, store);
                    if res:
                        return res;
                    store[h]-=1;
            
            return [];
    
        return helper(people, [], key, store);
        """
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])
        res = []
        for p in people:
            res.insert(p[1], p)
        return res