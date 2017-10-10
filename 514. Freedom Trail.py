class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        if not ring or not key:
            return 0;
        
        store = [0]*len(ring);
        
        cands = [0]
        for i, c in enumerate(key):
            new_cands = [idx for idx in range(len(ring)) if ring[idx]==c];
            #print c, new_cands
            for idx in new_cands:
                store[idx]=min([min(abs(cand-idx), len(ring)-abs(cand-idx))+store[cand] for cand in cands]);
                #for cand in cands:
                #    store[idx]+=abs(cand-idx);
            cands = new_cands;
        
            #print store
        return min([store[idx] for idx in cands])+len(key);
                        