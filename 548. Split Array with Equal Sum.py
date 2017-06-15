class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<5:
            return False;
        
        P = [0]
        for x in nums:
            P.append(P[-1]+x);
        
        Pinv = collections.defaultdict(list);
        for i, s in enumerate(P):
            Pinv[s].append(i)
            
        
        for j in range(1,len(nums)-1):
            for k in range(j+1, len(nums)-1):
                for i in Pinv[P[-1]-P[k+1]]:
                    if i>=j:
                        break;
                    if P[i]==P[j]-P[i+1]==P[k]-P[j+1]:
                        return True;
        
        return False;