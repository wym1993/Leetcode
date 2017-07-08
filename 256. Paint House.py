class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0;
        
        for i in range(1,len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2]) 
            costs[i][1] += min(costs[i-1][0], costs[i-1][2]) 
            costs[i][2] += min(costs[i-1][0], costs[i-1][1]) 
        
        size = len(costs)-1;
        return min(costs[size][0], costs[size][1], costs[size][2]);
        