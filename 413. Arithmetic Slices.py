class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0;
        
        res = 0;
        curr = 0;
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                curr+=1;
                res+=curr;
            else:
                curr = 0;
        return res;
        