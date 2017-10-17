class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs or not pairs[0]:
            return 0;
        
        pairs.sort(key = lambda x:x[0])
        
        dp = [1]*len(pairs);
        dp[0] = 1;
        
        for i in range(1, len(pairs)):
            cands = [dp[j] for j in range(i) if pairs[j][1]<pairs[i][0]]
            if cands:
                dp[i] = max(dp[i], max(cands)+1)
        
        return dp[-1];
        